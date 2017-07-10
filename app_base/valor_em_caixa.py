__author__ = 'Carlos'
from app_base.models import *
receitas = entradas()
despesas = saidas()

def saldo():
   if receitas.valor_entrada==None and despesas.valor_saida==None:
       return 0.0

   elif receitas.valor_entrada!=None and despesas.valor_saida==None:
       return int(receitas.valor_entrada)

   elif receitas.valor_entrada!=None and despesas.valor_saida!=None:
       return int(receitas.valor_entrada)-int(despesas.valor_saida)

def contas():
    pass