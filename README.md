# Auditoria de documentos com maturidade cognitiva

Este projeto audita centenas de documentos (Markdown e texto) para estimar a maturidade cognitiva com base em sinais como justificativas, evidências, alternativas e reflexões.

## Modelos finais de comercialização

O arquivo `modelos_comercializacao.md` reúne modelos prontos para uso com checklists e campos preenchíveis para diferentes estratégias comerciais.

## Como usar

```bash
python audit.py > relatorio.csv
```

O relatório CSV inclui o caminho do documento, o score de maturidade e os sinais detectados.
