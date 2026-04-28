from datetime import date, timedelta
import subprocess
import platform
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
    if not diretorio.strip():
        diretorio = os.path.join(os.getcwd(), "notas")
        print(f"Foi dado continuidade ao programa sem especificar o diretorio, foi criado uma pasta notas no diretorio {diretorio}")
    sistema = platform.system()
    if sistema == "Windows":
        invalid_directory = ["C:\\Windows", "C:\\System32"]
    elif sistema == "Darwin":
        invalid_directory = ["/System", "/Library"]
    else:  # Linux
        invalid_directory = ["/etc", "/usr", "/bin", "/sbin"]
    diretorio_absoluto = os.path.abspath(diretorio)
    if any(diretorio_absoluto.startswith(os.path.abspath(pasta)) for pasta in invalid_directory):
        print("Não é recomendado criar pastas ou arquivos em partes dedicadas ao sistema")
        continue
    if len(diretorio) > 300:
        print("Caminho muito longo, por favor usar no maximo 300 caracteres")
        continue
        
        
    try:
        if not os.path.isdir(diretorio):
            directory_confirm = input(f"Confirma a criação da pasta em {diretorio} ? (S/N)").upper()
            
            if directory_confirm == "S":
                os.makedirs(diretorio)
                print(f"Diretorio criado em {diretorio}, continuando...")
            else:
                print("Criação de pasta cancelada, por favor insira novamente onde deseja criar a pasta:")
                continue
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
            elif len (topico) > 150:
                print("Caminho longo demais, por favor respeitar o limite de 150 caracteres")
            else:
                topicos.append(topico)
                print(f"O topico {i+1} de {topico_quantidade} adicionado")
                print("\nSeguindo com a execução do programa\n")
                break
    while True:
        Type_of_text = input("Qual formato de texto deseja usar? (md/txt): ").lower()
        if Type_of_text in ["md", "txt"]:
            break
        print ("Formato invalido ou incompleto, escolha md ou txt")
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
            dia_atual = Hoje
            topicos = []
            diretorio = ""
            Type_of_text = ""
            print("\nEntendido, reiniciando sistema de escolha...\n")
            break
        else:
            print("Resposta invalida, por favor digite S ou N para responder")

while dia_atual <= Fim:
    nome_formatado = dia_atual.strftime("%Y-%m-%d %A").title()
    nome_arquivo = f"{nome_formatado}.{Type_of_text}"
    caminho_total = os.path.join(diretorio, nome_arquivo)
    if not os.path.exists(caminho_total):
        try:
            with open(caminho_total, "w", encoding="utf-8") as f:
                for topico in topicos:
                    f.write(f"\n\n\n## {topico}:\n\n\n")
            print(f"Topicos adicionados ao arquivo {nome_arquivo}")
        except OSError:
            print(f"Houve um erro, não foi possivel criar um arquivo")
    else:
        print(f"Arquivo {nome_arquivo} ja existe, etapa de criação pulada....")
    dia_atual += timedelta(days=1)
print("\nARQUIVO GERADO E FORMATADO COM SUCESSO")
while True:
    abrir = input("Deseja abrir a pasta? (S/N) ").upper()
    if abrir == "S":
        sistema = platform.system()
        if sistema == "Windows":
            os.startfile(diretorio)
        elif sistema == "Darwin":
            subprocess.run(["open", diretorio])
        else:
            subprocess.run(["xdg-open", diretorio])
        break
    elif abrir == "N":
        break
    else:
        print("Resposta inválida, digite S ou N")