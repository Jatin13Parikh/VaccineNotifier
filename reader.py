import configparser

#  Load and Read the configuration file
config = configparser.RawConfigParser()
configFilePath = r'D:\Python-Practice\VaccineNew\VaccineNotifier\config.txt'
config.read(configFilePath)

PINCODE = config.get('userData', 'PINCODE')
EMAIL = config.get('userData', 'EMAIL')
AGE = config.get('userData', 'AGE')