import scrapy

class JobsSpider(scrapy.Spider):
    name = "jobs"

    start_urls = [
        "https://realpython.github.io/fake-jobs/"
    ]

    def parse(self, response):
        jobs = response.css("div.card-content")

        for job in jobs:
            yield {
                "title": job.css("h2.title::text").get(default="N/A").strip(),
                "company": job.css("p.subtitle.is-6.company::text").get(default="N/A").strip(),
                "location": job.css("p.location::text").get(default="N/A").strip(),
                "date": job.css("time::attr(datetime)").get(default="N/A"),
                "url": job.css("a.card-footer-item::attr(href)").get(default="N/A")
            }