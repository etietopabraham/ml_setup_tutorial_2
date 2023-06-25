import sys 

# logger

def error_message_details(error, error_detail:sys)->str:
    _,_,exc_tb = error_detail.exc_info()
    error_message = "Error occured in your python script name [{0}], line number [{1}], error message [{2}]".format(
        exc_tb.tb_frame.f_code.co_filename, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_mesage, error_details:sys):
        super().__init__(error_mesage)
        self.error_message = error_message_details(error=error_mesage, error_detail=error_details)

    def __str__(self):
        return self.error_message
    

# ## Test
# if __name__ == "__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logger.logging.info("Exception, divide by zero")
#         raise CustomException(e, sys)
