# Auto-Archive-Gen
Gerador de arquivos e pastas automático baseado no ano, mês, dia do usuário

## Sobre o projeto
O Auto Archive Gen é um gerador de notas feito para resolver problemas do cotidiano relacionado a anotações, sendo essencial para qualquer pessoa que deseja se organizar de forma **rapida**, **pratica** e **automatica**.

## Como usar
1. Tenha Python 3 instalado
2. Execute o arquivo `DateTimer.py` no terminal (pode ser acessado em <https://www.python.org/downloads/>)
3. Siga as instruções na tela

## Requisitos
- Python 3
- Bibliotecas: `datetime`, `calendar`, `locale`, `os` (já inclusas no Python)

## Historico de atualizações lançadas

### v0.3.0
- Suporte a formato txt além de md
- Confirmação antes de criar pasta
- Pergunta se deseja abrir a pasta após criação
- Suporte cross-platform para abrir pasta (Windows, Mac, Linux)
- Verificação de pastas do sistema (impede criar em pastas críticas)
- Limite de caracteres para diretório (300) e tópicos (150)
- Ordenação das validações de diretório corrigida
- Reset de variáveis ao reiniciar ciclo

## v.0.2.5
- Adicionado limite de caracteres
- Correção de espaçamento 

## v0.2.4
- Trocado exists () por isdir()
- Trocado .capitalize por .title() para abranger string completa
- Adicionar if not topico.strip() para remover espaços em brancos e remover if topico ==" ":

### v0.2.1
- Limpar topicos/diretorio ao reiniciar	
- Tratamento de locale caso haja falha	
- Tratamento de erro no with open	
- Correção de indentação	

### v0.1.0
- Locale automático pelo idioma da máquina
- Pasta padrão "notas" quando diretório vazio
- Proteção contra inputs inválidos no número de tópicos
- Limite máximo de 50 tópicos
- Proteção contra tópico vazio
- Validação de diretório inválido
- Feedback de progresso ao adicionar tópicos
- Validação de resposta S/N

### v0.0.1
- Geração automática de arquivos .md do dia atual até fim do mês
- Tópicos personalizáveis via input
- Verificação de sobrescrita
- Confirmação de dados antes de executar

## Previsão de futura atualização
- suporte a txt além de md 
- Template de tópicos pré-definidos
- Confirmação antes de criar pasta nova 
- Abrir nota ou pasta após criação 