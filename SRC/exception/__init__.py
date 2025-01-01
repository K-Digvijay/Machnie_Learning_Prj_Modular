import os, sys

class CustomException(Exception):
    def __init__(self,error_message:Exception, error_details:sys):
        self.error_message = CustomException.Get_Detail_Error_Message(error_message=error_message,
                                                                      error_details=error_details)

# try:
#     pass
# exception:
#     pass
    @staticmethod
    def Get_Detail_Error_Message(error_message:Exception, error_details:sys)->str:
        _,_, exce_try_block = error_details.exc_info()

        exception_block_line_number = exce_try_block.tb_frame
        try_block_line_number = exce_try_block.tb_lineno

        file_name = exce_try_block.tb_frame.f_code.co_filename

        error_message =f"""
        Error ocured in exception of:
        [{file_name}] at 
        try block number : [{try_block_line_number}]
        and exception block line number : [{exception_block_line_number}]
        error message : [{error_message}]

        """
        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__.str()
