from scrapy import Spider,Request
import urllib.parse as urlparse

class Coupons(Spider):
	name = 'coupons'
	start_urls = [
					'https://smartybro.com/category/udemy-coupon-100-off/',
					'https://comidoc.net/coupons',
					'https://udemycoupon.learnviral.com/',
					'https://www.real.discount/store/udemy/'
					]
	def start_requests(self):
		for url in self.start_urls:
			if url == 'https://smartybro.com/category/udemy-coupon-100-off/':
				yield Request(url , callback=self.parse_smartybro)
			elif url == 'https://comidoc.net/coupons':
				yield Request(url , callback=self.parse_comidoc)
			elif url == 'https://udemycoupon.learnviral.com/':
				yield Request(url , callback=self.parse_learnviral)
			else :
				yield Request(url , callback=self.parse_realdiscount)

	def parse_smartybro(self,response):
		all_items = response.css('div.item')[0]
		course_names = all_items.xpath('//div/h2[@class="grid-tit"]/a/text()').extract()
		course_span_tags = all_items.xpath('//div/p[3]/span[@class="tag-post"]')
		course_tags = []
		course_coupons = []
		coupon_links = all_items.xpath('//a[@class="more-link"]/@href').extract()
		for i in range(0,len(course_span_tags)):
			course_tags.append(course_span_tags[i].css('a::text').extract())
		for i in range(0,len(coupon_links)):
			course_coupons.append(Request("".join(coupon_links[i]), callback = self.parse_smartybro_coupon_links))

			
		yield {'course_names':course_names,'course_tags':course_tags,
				'coupon_links':coupon_links,'coupons':course_coupons}

	def parse_smartybro_coupon_links(self,response):
		# coupon_button = response.xpath('//a[@class="fasc-type-flat"]/@onclick').extract_first()
		# yield coupon_button
		print('hello')

		
	def parse_comidoc(self,response):
		print(2)
	def parse_learnviral(self,response):
		print(3)
	def parse_realdiscount(self,response):
		print(4)

