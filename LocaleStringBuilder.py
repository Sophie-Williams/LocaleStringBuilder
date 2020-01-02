__author__ = "Owsap"
__copyright__ = "Copyright 2020, Owsap Productions"
__license__ = "GPL"
__version__ = "1.0.0"

import os
import sys

localeStringFileName = "locale_string.txt"

def GetLocaleStringFile(locale):
	return "%s/%s" % (locale, localeStringFileName)

def TransalteLocaleString(locale):
	localeStringOutput = "locale_string_%s.txt" % locale

	if os.path.exists(localeStringOutput):
		os.remove(localeStringOutput)

	fileOutput = open(localeStringOutput, 'a')

	for line in open(localeStringFileName, 'r'):
		split = line.split('";')
		vnum = split[0][1:]

		if not vnum:
			print ""
			fileOutput.write("")

		if not vnum.isdigit():
			formated = split[0] + "\";"
			print (formated.rsplit("\n", 3)[0])
			fileOutput.write(formated.rsplit("\n")[0] + "\n")
			continue

		print GetTranslationVnum(locale, vnum)
		fileOutput.write(GetTranslationVnum(locale, vnum) + "\n")

	fileOutput.close()

def GetTranslationVnum(locale, vnum):
	lineCount = 0
	for line in open(GetLocaleStringFile(locale), 'r'):
		lineCount += 1
		match = line.find(vnum)
		if match == 0:
			localeStringFile = open(GetLocaleStringFile(locale), 'r')
			localeText = str(localeStringFile.readlines()[lineCount - 1])
			split = localeText.split("\t")
			formated = "\"" + split[1]

			return (formated.rsplit("\n", 3)[0]) + "\";"

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "USAGE: [locale]"
		locale = raw_input("Enter locale name: ")
		TransalteLocaleString(str(locale))

	elif len(sys.argv) == 2:
		TransalteLocaleString(sys.argv[1])