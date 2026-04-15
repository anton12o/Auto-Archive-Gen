from datetime import date, timedelta
import calendar
import locale 
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
import os

Hoje = date.today()
_, mes_fim = calendar.monthrange(Hoje.year, Hoje.month)
Fim = date(Hoje.year, Hoje.month, mes_fim)
dia_atual = Hoje

diretorio = input ("Digite o diretorio que deseja salvar os documentos: ")
if not os.path.exists(diretorio):
    os.makedirs(diretorio)
    print(f"O diretorio não foi encontrado o diretorio em {diretorio} em uma primeira busca, porem agora esta criado em {diretorio} ")
else:
    print(f"Diretorio {diretorio} localizado, continuando com o processo...")

topico_quantidade = int(input ("Quantos topicos deseja adicionar?"))

topicos = []
for i in range(topico_quantidade):
  topico = input("Qual topico deseja adicionar?")  
  topicos.append(topico)
while dia_atual <= Fim:
       nome_formatado = dia_atual.strftime ("%Y-%m-%d %A").capitalize()
       nome_arquivo = f"{nome_formatado}.md"
       caminho_total = os.path.join(diretorio, nome_arquivo)
       if not os.path.exists(caminho_total):
        with open (caminho_total, "w", encoding="utf-8") as f:
         for topico in topicos :
            f.write(f"\n\n\n##{topico}:\n\n\n")
       dia_atual += timedelta(days=1)
print ("\nARQUIVO GERADO E FORMATADO COM SUCESSO")
    
