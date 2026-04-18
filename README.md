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

### v1.5
- Locale automático pelo idioma da máquina
- Pasta padrão "notas" quando diretório vazio
- Proteção contra inputs inválidos no número de tópicos
- Limite máximo de 50 tópicos
- Proteção contra tópico vazio
- Validação de diretório inválido
- Feedback de progresso ao adicionar tópicos
- Validação de resposta S/N

### v1.0
- Geração automática de arquivos .md do dia atual até fim do mês
- Tópicos personalizáveis via input
- Verificação de sobrescrita
- Confirmação de dados antes de executar

## Futuras atualizações
- [ ] Suporte a `txt`, `pdf`, `xlsx`
- [ ] Criação automática de pasta por mês
- [ ] Interface gráfica
- [ ] Exportar como `.exe`
