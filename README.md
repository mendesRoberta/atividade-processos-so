# atividade-processos-so

# Atividade Prática – Processos Pai, Filhos e Zumbis

**Aluna:** Roberta Mendes Monteiro
**Disciplina:** Sistemas Operacionais
**Professor:** Rosinei de Sousa Oliveira

# Descrição

Este repositório contém os três scripts em Python desenvolvidos para a atividade prática sobre gerenciamento de processos em sistemas operacionais. Cada script simula um cenário específico conforme solicitado.

---

# Cenário A: Execução Normal

**Arquivo:** `cenario_a_normal.py`
**Descrição:** Este script demonstra a criação de dois processos filhos por um processo pai. O pai aguarda (`os.wait()`) o término de ambos os filhos antes de finalizar sua própria execução.
**Como Executar:** `python3 cenario_a_normal.py`
**Saída Esperada:** A saída mostrará as mensagens do pai e dos filhos, com a mensagem final do pai sempre aparecendo por último.

---

# Cenário B: Processos Órfãos

**Arquivo:** `cenario_b_orfao.py`
**Descrição:** Neste cenário, o processo pai cria dois filhos e termina imediatamente, sem aguardá-los. Os filhos continuam em execução e são "adotados" por um processo do sistema (como o `systemd --user`), o que pode ser observado pela mudança em seu PPID.
**Como Executar:** `python3 cenario_b_orfao.py`
**Saída Esperada:** A saída dos filhos mostrará que o PPID (ID do processo pai) muda após um tempo, provando a adoção.

---

# Cenário C: Processo Zumbi

**Arquivo:** `cenario_c_zumbi.py`
**Descrição:** O script cria um filho que termina imediatamente. O processo pai, no entanto, continua vivo por 30 segundos sem chamar `os.wait()`, mantendo o filho em um estado "zumbi".
* **Como Executar e Observar:**
    1.  Em um terminal, execute: `python3 cenario_c_zumbi.py`
    2.  Em um segundo terminal, enquanto o script está pausado, execute `ps aux | grep 'Z+'` para visualizar o processo filho no estado `<defunct>`.
