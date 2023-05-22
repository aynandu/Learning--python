from selenium import  webdriver
chrom_Driver = webdriver.Chrome('./chromedriver')
chrom_Driver.maximize_window()
chrom_Driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')