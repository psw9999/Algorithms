#######################################################################################################################
#
# Dart 크롤링 모듈
#   2022-01-27
#
# 할일
#   개 쓰잘데기없는 놈들 크롤링되는데 해결보기 (실권주)
#   데이터베이스 로직 작성
#
#######################################################################################################################
import OpenDartReader
from xml.etree.ElementTree import Element, SubElement, ElementTree, dump
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
import datetime
import pandas as pd
# pd.set_option('display.max_columns', None)  # 모든 열을 출력한다.

class DartCrawling:
    target_report = [['R00', '증권발행실적보고서'],
                     ['R01', '증권신고서(지분증권)'],
                     ['R02', '[기재정정]증권신고서(지분증권)'],
                     ['R03', '[발행조건확정]증권신고서(지분증권)']]
    report_name = ""

    def __init__(self, api_key):
        self._dart = OpenDartReader(api_key)
        report_name = self.target_report[0][1]  # 필터링할 보고서이름 모음
        for i in range(0, len(self.target_report)):
            report_name = report_name + "|" + self.target_report[i][1]

    # 해당 일자의 원하는 증권신고서만 가져오기
    # 입력 : 공시보고서 발행일 (0000-00-00)
    # 출력 : List 0보고서번호, 1보고서명, 2기업코드, 3기업이름
    def list_report(self, date):
        reports = self._dart.list(start=date, end=date, final=False)  # 전체보고서 가져오기
        s = (reports.report_nm.str.contains(self.report_name))  # 원하는 보고서만 가져오기(보고서명 기준)
        reports = reports.loc[s, :]

        list_report = (list(reports.rcept_no), list(reports.report_nm), list(reports.corp_code), list(reports.corp_name))
        return list_report

    # 이름에 따른 증권신고서 분류
    # 입력 : 보고서명 (str)
    # 출력 : 보고서 분류 코드 (str)
    def kind_report(self, report_name):
        report_name = re.sub(r'\s+', '', repor2t_name)  # 공백제거
        for i in range(0, len(self.target_report)):
            if report_name in self.target_report[i][1]:
                return self.target_report[i][0]
        return "E00"

    # 보고서 내에 원하는 메뉴의 HTML BODY값을 RETURN
    # 입력 : 보고서번호, 조회할메뉴이름(DART 좌측 메뉴들..)
    # 출력 : 해당메뉴 html page의 body값
    def document_body(self, report_number, menu_name):
        subDocs = self._dart.sub_docs(report_number, menu_name)
        subDoc = list(subDocs.url)

        # print(subDoc[0])  # 주소 출력
        report = urlopen(subDoc[0])
        r = report.read()
        xmlsoup = BeautifulSoup(r, 'html.parser')
        body = xmlsoup.find("body")
        return body

    # 각 보고서별 로직 실행
    # 입력 : 보고서 분류 코드 (str), 보고서 번호 (str)
    # 출력 : dict (필수값(type): 보고서코드(str data) 및 해당 데이터들)
    def report_to_dict(self, report_code, report_number):
        if report_code in "E00":
            raise Exception('E00: 지정된 형식과 일치하는 보고서가 아닙니다. ' + report_code)
            
        print("타입: ", report_code, "보고서번호: ", report_number)
        if report_code in "R00":
            return self.__r00_logic(report_number)
        elif report_code in "R01":
            return self.__r01_logic(report_number)
        elif report_code in "R02":
            return self.__r02_logic(report_number)
        elif report_code in "R03":
            return self.__r03_logic(report_number)

    # 입력 : 보고서 번호 (str)
    # 출력 : dict
    def __r00_logic(self, report_number):
        html_body = self.document_body(report_number, "증권교부일 등")

        # 페이지에 특정 태그 데이터를 가져온다.
        summarizeTable = html_body.find_all("p")
        summarizeTable = (str(summarizeTable))
        # print(summarizeTable)

        # 가장 마지막에 있는 날짜 정보를 사용한다.
        port_regex = re.findall(
            "(2020|2021|2022)[- /.년]*([1-9]|0[1-9]|1[012])[- /.월]*([1-9]|0[1-9]|[12][0-9]|3[01])[- /.일]",
            summarizeTable)
        end_point = port_regex.pop()
        d = datetime.datetime.strptime(str(end_point), "('%Y', '%m', '%d')")

        #dict 출력
        dict = {"ipo_debut_date": d.strftime("%Y-%m-%d")}
        return dict

    def __r01_logic(self, report_number):  # 증권신고서(지분증권) - 최초
        return self.__r02_logic(report_number)
        
    def __r02_logic(self, report_number):  # [기재정정]증권신고서(지분증권) - 정정
        profit, sales = 0, 0 
        html_body = self.document_body(report_number, "모집 또는 매출에 관한 일반사항")
        summarizeTable = html_body.find_all("tr")
        
        html_body2 = self.document_body(report_number, "재무에 관한 사항")
        summarizeTable2 = html_body2.find_all("tr")
        
        dict = {'profit' : 0, 'sales' : 0, 'stockQuantity' : 0,'ipo_price_low' : 0, 'ipo_price_high' : 0}
        financial_company = {}
        
        # 영업이익, 매출액 크롤링 (재무에 관한 사항)
        for s in summarizeTable2 :
            temp = s.find_all("td")
            if len(temp) < 2 :
                continue
            if "매출액" in temp[0].get_text():
                sales = temp[1].get_text().replace(',','').rstrip()
            elif "영업이익" in temp[0].get_text():
                profit = temp[1].get_text().replace(',','').rstrip()
            if profit != 0 and sales != 0 :
                break
        
        # 증권사별 배정 물량 (모집 또는 매출에 관한 일반사항)
        for s in range(len(summarizeTable)):
            temp = summarizeTable[s].find_all("th")

            if len(temp) < 4:
                continue

            if "배정물량" in temp[1].get_text().replace(" ", ""):
                temp_td = summarizeTable[s + 1].find_all("td")
                if len(temp_td) > 3:
                    company = temp_td[0].get_text().replace("\xa0", "")
                    #print(company)
                    limit = temp_td[2].get_text().replace("\n", "").replace(" ", "")
                    # 다음 td에 청약 최고 한도 서술되어 있음

                    # if re.compile('[가-힣]+').findall(limit) == ['주']:
                    temp_td2 = summarizeTable[s + 2].find_all("td")  # 다음 tr 값에 주) 에 대한 내용이 있음
                    limit2 = ' '.join(temp_td2[1].get_text().split())  # 개행문자, 띄워쓰기 중복 등 제거
                    limit3 = limit2.replace(',', '').replace(' ', '').replace('주~', '~')  # (숫자)주~(숫자)주 를 찾기위해 ,와 공백문자 제거 and 주~ 을 ~로 변환
                    limit4 = re.findall(r'일반|우대|\d{2,3}%|\d{2,10}~\d{2,10}주', limit3)  # (숫자)주~(숫자)주 정규식 찾기
                    limit5 = ''
                    #print(limit4)
                    try:
                        for i in range(len(limit4)):
                            if limit4[i] == '일반':
                                if limit4[i + 1] == '100%':
                                    limit5 = limit4[i + 2]
                                    #print(limit5)
                                elif limit4[i + 1].find("주") == -1:
                                    continue
                                else:
                                    limit5 = limit4[i + 1]
                                    #print(limit5)
                                    break
                            else:
                                continue

                        limit6 = []  # 숫자에 , 찍기
                        for num in limit5.replace('주', '').split('~'):  # 주 를 빼고 ~로 숫자를 나눔
                            limit6.append(format(int(num), ',d'))  # 숫자에 콤마찍음

                        financial_company[company] = [temp_td[1].get_text().replace("\n", "").replace(" ", "").replace("\xa0", "").replace(",", "").replace("주", ""),
                                                    str(limit6[0]).replace(",", "") + '~' + str(limit6[1]).replace(",", "").replace("주", "")]

                    except ValueError as e:
                        financial_company[company] = [temp_td[1].get_text().replace("\n", "").replace(" ", "").replace("\xa0", "").replace(",", "").replace("주", ""),
                                                    temp_td[2].get_text().replace("\n", "").replace(" ", "").replace(",", "").replace("주", "")]
        
        # 상단,하단 밴드 (모집 또는 매출에 관한 일반사항)                
        for s in range(len(summarizeTable)) :
            temp = summarizeTable[s].find_all("th")
            temp2 = summarizeTable[s].find_all("td")
            if len(temp) > 1:
                focus_word_hopeprice = re.sub(r'\s+', '', temp[0].get_text())
                if "희망공모가액" in focus_word_hopeprice:
                    temp_td = summarizeTable[s].find_all("td")
                    if len(temp_td) > 1:
                        hopeprice = temp_td[1].get_text()

            elif len(temp2) > 1:
                focus_word_hopeprice = re.sub(r'\s+', '', temp2[0].get_text())
                if "희망공모가액" in focus_word_hopeprice:
                    temp_td = summarizeTable[s].find_all("td")
                    if len(temp_td) > 1:
                        hopeprice = temp_td[1].get_text()
        
        hopeprice = hopeprice.replace(",", "").replace("원", "")
        hope = re.findall(r'\d{1,100}', hopeprice)
        
        dict["profit"] = profit
        dict["sales"] = sales
        dict['stockQuantity'] = financial_company.copy()
        dict["ipo_price_low"] = hope[0]
        dict["ipo_price_high"] = hope[1]
        return dict

    def __r03_logic(self, report_number):  # [발행조건확정]증권신고서(지분증권)
        html_body = self.document_body(report_number, "증권발행조건확정")
        summarizeTable = html_body.find_all("tr")
        summarizeTable = (str(summarizeTable))

        sales = 0
        acceptance_rate = 0.0
        for s in range(len(summarizeTable)):
            temp = summarizeTable[s].find_all("th")
            temp2 = summarizeTable[s].find_all("td")
            if len(temp) > 3:
                # 모집(매출)가액 문자열을 잘 가공하세요
                focus_word_arate = re.sub(r'\s+', '', temp[0].get_text())
                focus_word_price = re.sub(r'\s+', '', temp[3].get_text())
                if "모집(매출)" in focus_word_price:
                    temp_td = summarizeTable[s + 1].find_all("td")
                    if len(temp_td) > 3:
                        sales = re.sub(r'[^0-9]', '', temp_td[3].get_text())
                elif "경쟁률" in focus_word_arate:
                    temp_td = summarizeTable[s].find_all("td")
                    acceptance_rate = float(temp_td[7].get_text().replace(',', ''))

            elif len(temp2) > 3:
                focus_word_arate = re.sub(r'\s+', '', temp2[0].get_text())
                focus_word_price = re.sub(r'\s+', '', temp2[3].get_text())
                if "모집(매출)" in focus_word_price:
                    temp_td = summarizeTable[s + 1].find_all("td")
                    if len(temp_td) > 3:
                        sales = re.sub(r'[^0-9]', '', temp_td[3].get_text())
                elif "경쟁률" in focus_word_arate:
                    temp_td = summarizeTable[s].find_all("td")
                    acceptance_rate = float(temp_td[7].get_text().replace(',', ''))

            if "확약" in temp2[0].get_text().replace(" ", ""):
                temp_td = summarizeTable[s + 5].find_all("td")
                temp_td2 = summarizeTable[s + 4].find_all("td")
                notMustHave = int(temp_td2[14].get_text().replace(',', ''))
                haveSum = int(temp_td[14].get_text().replace(',', ''))
                print((haveSum - notMustHave) / haveSum * 100)

        dict = {"ipo_price": sales, "ipo_institutional_acceptance_rate": acceptance_rate}
        return dict


#######################################################################################################################
#
# 메인문
#
#######################################################################################################################
if __name__ == "__main__":
    dart = DartCrawling("a5f0a27ad384e3e1af8ea81c2f0be00a419bfb1e")
    report_list = dart.list_report("2022-01-05")  # datetime.datetime.now()
    report_number = report_list[0]
    report_name = report_list[1]
    dart_code = report_list[2]
    company_name = report_list[3]

    for i in range(0, len(report_number)):
        rcode = dart.kind_report(report_name[i])
        rnum = report_number[i]
        rdartcode = dart_code[i]
        rcpname = company_name[i]

        try:
            dict = dart.report_to_dict(rcode, rnum)
            dict["rcode"] = rcode
            dict["rdartcode"] = rdartcode
            dict["rcpname"] = rcpname
            print(dict)
        except Exception as e:
            pass
            #print(e)
