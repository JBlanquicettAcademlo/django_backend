# try:
#     print(1/1)
# except ZeroDivisionError:
#     print('No se puede dividir entre cero')
# else:
#     print('no se ha generado nda, todo cool')
# finally:
#     print('siempre..')

class AcademloException(BaseException):
    ...

raise AcademloException('Students cannot pass python course less than 70%')