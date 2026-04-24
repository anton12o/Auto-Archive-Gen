from datetime import date, timedelta
import calendar
import locale
import os

try:
    locale.setlocale(locale.LC_ALL, "")
except locale.Error:
    pass

Hoje = date.today()
_, mes_fim = calendar.monthrange(Hoje.year, Hoje.month)
Fim = date(Hoje.year, Hoje.month, mes_fim)
dia_atual = Hoje


confirmado = False
while not confirmado:

    diretorio = input("Digite o diretorio que deseja salvar os documentos: ")
    if diretorio == "":
        diretorio = os.path.join(os.getcwd(), "notas")
        print(
            f"Foi dado continuidade ao programa sem especificar o diretorio, então foi criado uma pasta notas no diretorio {diretorio}"
        )

    try:
        if not os.path.isdir(diretorio):
            os.makedirs(diretorio)
            print(
                f"O diretorio não foi encontrado o diretorio em {diretorio} em uma primeira busca, porem agora esta criado em {diretorio} "
            )
        else:
            print(f"Diretorio {diretorio} localizado, continuando com o processo...")
    except OSError:
        print("Diretorio selecionado invalido, por favor tente novamente")
        confirmado = False
        continue

    while True:
        try:
            topico_quantidade = int(input("Quantos topicos deseja adicionar?"))
            if topico_quantidade <= 0 or topico_quantidade > 50:
                raise ValueError
            print(
                f"Foram adicionados uma quantidade {topico_quantidade} topicos no diretorio {diretorio}"
            )
            break
        except ValueError:
            print(
                "Esta resposta não é valida, selecione um valor valido ou acima de 0 e menor que 50..."
            )

    topicos = []
    for i in range(topico_quantidade):
        while True:
            topico = input("Qual topico deseja adicionar?")
            if not topico.strip():
                print("Valor vazio, por favor insira um valor valido")
            else:
                topicos.append(topico)
                print(f"O topico {i+1} de {topico_quantidade} adicionado")
                print("\nSeguindo com a execução do programa\n")
                break
    print("\n---VALIDAÇÃO DE INFORMAÇÕES---\n")
    print(f"Diretorio: {diretorio}")
    print(f"Quantidade de tópicos: {topico_quantidade}")
    print(f"Tópicos: {', '.join(topicos)}")
    while True:
        confirmar = input("\nConfirma os dados acima? (S/N)").upper()

        if confirmar == "S":
            confirmado = True
            break
        elif confirmar == "N":
            print("\nEntendido, reiniciando sistema de escolha...\n")
            break
        else:
            print("Resposta invalida, por favor digite S ou N para responder")

while dia_atual <= Fim:
    nome_formatado = dia_atual.strftime("%Y-%m-%d %A").title()
    nome_arquivo = f"{nome_formatado}.md"
    caminho_total = os.path.join(diretorio, nome_arquivo)
    if not os.path.exists(caminho_total):
        try:
            with open(caminho_total, "w", encoding="utf-8") as f:
                for topico in topicos:
                    f.write(f"\n\n\n##{topico}:\n\n\n")
            print(f"Topicos adicionados ao arquivo {nome_arquivo}")
        except OSError:
            print(f"Houve um erro, não foi possivel criar um arquivo")
    else:
        print(f"Arquivo {nome_arquivo} ja existe, etapa de criação pulada....")
    dia_atual += timedelta(days=1)
print("\nARQUIVO GERADO E FORMATADO COM SUCESSO")
