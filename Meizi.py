#coding: utf-8
import argparse
import urllib
import os
import requests
from MyThread import MyThread
from urllib import request
from bs4 import BeautifulSoup

def get_html(url_address):
	"""
	通过url_address得到网页内容
	:param url_address: 请求的网页地址
	:return: html
	"""
	headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv: 23.0) Gecko/20100101 Firefox/23.0'}
	req = urllib.request.Request(url=url_address, headers=headers)
	return urllib.request.urlopen(req)
	

def get_soup(html):
	"""
	把网页内容封装到BeautifulSoup中并返回BeautifulSoup
	:param html: 网页内容
	:return:BeautifulSoup
	"""
	if None == html:
		return
	return  BeautifulSoup(html.read(), "html.parser")
	

def get_img_dirs(soup):
	"""
	获取所有相册标题及链接
	:param soup :BeautifulSoup实例
	:return: 字典 (key:标题， value：内容)
	"""
	if None == soup
	    return
	lis = soup.find(id="pins").findAll(name='li')
	if None != lis:
		img_dirs = {}
		for li in lis:
			links = li.find('a')
			k = links.find('img').attrs['alt']
			t = links.attrs['href']
            img_dirs[k] = t;
        print(img_dirs)
        return img_dirs

