import requests
from bs4 import BeautifulSoup

URL = "http://www.saramin.co.kr/zf_user/jobs/list/job-category?page=1&cat_key=40426%2C40430&exp_cd=1&exp_none=y&job_type=1%2C4%2C2&search_optional_item=y&search_done=y&panel_count=y&sort=RD&tab_type=all&cat_nm%5B40426%5D=%EC%9B%B9%EA%B0%9C%EB%B0%9C+%3E+Python&cat_nm%5B40430%5D=%EC%9B%B9%EA%B0%9C%EB%B0%9C+%3E+%EB%B0%B1%EC%97%94%EB%93%9C&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=4&recruit_kind=recruit&quick_apply=n&isAjaxRequest=0&page_count=50&type=job-category&is_param=1#searchTitle"
URL_F = f"http://www.saramin.co.kr/zf_user/jobs/list/job-category?page="

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class":"pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_job(html):
    title = html.find("div", {"class":"col notification_info"}).find("div", {"class":"job_tit"}).find("a")["title"]
    company = html.find("div", {"class":"col company_nm"}).find("a")["title"]
    location = html.find("div", {"class":"col company_info"}).find("p", {"class":"work_place"}).string
    job_id = html.find("div", {"class":"col notification_info"}).find("div", {"class":"job_tit"}).find("a")["href"]
    return {'title': title,'company': company, 'location': location, 'link': f"http://www.saramin.co.kr{job_id}"}

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping saramin {page}")
        result = requests.get(f"{URL_F}{page+1}&cat_key=40426%2C40430&exp_cd=1&exp_none=y&job_type=1%2C4%2C2&search_optional_item=y&search_done=y&panel_count=y&sort=RD&tab_type=all&cat_nm%5B40426%5D=%EC%9B%B9%EA%B0%9C%EB%B0%9C+%3E+Python&cat_nm%5B40430%5D=%EC%9B%B9%EA%B0%9C%EB%B0%9C+%3E+%EB%B0%B1%EC%97%94%EB%93%9C&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=4&recruit_kind=recruit&quick_apply=n&isAjaxRequest=0&page_count=50&type=job-category&is_param=1#searchTitle")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"list_item"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs
    
def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs

