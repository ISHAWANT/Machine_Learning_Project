import os
import sys
class HousingException(Exception):
    def __init__(self, error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message=HousingException.get_detailed_error_message(error_message=error_message,error_detail=error_detail)
    
    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys) ->str:
        """
        error meassage: Exceoption object
        error details: object of sys module
        """
      
        _,_ ,exec_tb = error_detail.exc_info()

        line_number = exec_tb.tb_lineno
        file_name=exec_tb.tb_frame.f_code.co_filename

        error_message=f"Error occured in scrip: [{file_name}] at try block line number: [{try_block_line_number}] and exception block number: [{exception_block_number}] error message: [{error_message}]"
        return error_message
        
    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return HousingException.__name__.str()

    
