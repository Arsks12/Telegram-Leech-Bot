from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "7206702826:AAFiQoFSuXe4o1MVWkn77w0yEe_SmMIAVnY"
	APP_ID = 7068671
	API_HASH = "76c7e8041eaf80e335127a33b5618c96"
	OWNER_ID = "873713243" #ID of bot owner
	AUTH_CHANNEL = [-1002202897360]
	DESTINATION_FOLDER = "HelloMan" #Name of your folder read readme
	RCLONE_CONFIG = """[Arima 27]
type = drive
scope = drive
token = {"access_token":"ya29.a0AXooCguZ2WncJiQB8MIdkDpkzO4KXUB4ohGeZhNt306nzI3H-hRay5b6ToWUV3Fn_C6wq3T3_2uRFhV0znZV5xXQde4gmCOPoac3OX1dIc_WeYCFMtCfCFgpnRW8Jxp8dxbEzd35k5Y2E6QSFloVbNFJU2982mZLquywzAaCgYKAeYSARMSFQHGX2MinV0w9FT0WlaUYgFa7cMpIw0173","token_type":"Bearer","refresh_token":"1//0gBhhniNyOSHqCgYIARAAGBASNwF-L9Irs0HYbk9TtdwOTcv4zGeBQtPJ7oDVdiz8JT0aEv3yY57-9MXNYRdtf6Vyt7me4eVRQW4","expiry":"2024-07-28T16:56:52.6490397+05:30"}
team_drive = 0ANfpqOOWza3xUk9PVA
root_folder_id = """
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
