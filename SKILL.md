# Skill: ventura.build — LOOP Skill Engine / Deterministic Replay

![EPL-2.0](https://img.shields.io/github/license/chamseddinehiddoud/ventura.build)
![stars](https://img.shields.io/github/stars/chamseddinehiddoud/ventura.build)
![forks](https://img.shields.io/github/forks/chamseddinehiddoud/ventura.build)

Skill de aprendizado por reconstrução de ferramentas com **execução
determinística**: explore o projeto uma vez, compile o plano de construção,
replique etapa por etapa com ~zero tokens, regenere quando a arquitetura
mudar.

## Trigger

Use quando o usuário quiser: construir sua própria versão de uma ferramenta
(banco, servidor, shell, compilador, git), aprender por reconstrução, montar
projeto hands-on, comparar implementação própria com a real.

## Arquitetura Token-Efficient & Regenerative

| Fase | Descrição | Consumo |
|---|---|---|
| **Explore** | Modelo forte estuda o que a ferramenta faz (uma vez) | Alto (único) |
| **Compile** | Gera `projeto.md`: etapas, entregas, testes, arquitetura | Baixo |
| **Replay** | Implementa a próxima etapa — sem replanejar tudo | Mínimo/Zero |
| **Regenerate** | Erro de arquitetura/novo requisito → regenere o plano | Sob demanda |

## Receita determinística (Replay)

```text
1. PEDIDO   — "próxima etapa do projeto" | "implementar X"
2. RECEITA  — consulta projeto.md: etapa N, entrega, testes, arquitetura
3. EXECUTA  — 1. escreve a menor versão da etapa | 2. roda os testes
             3. confirma entrega executável
4. REGISTRA — etapa concluída, dificuldade, divergências do original
5. STOP-YIELD — etapa estoura o escopo → sinaliza regenerar o plano
```

## Regras de engenharia

- **Token Budget** — Explore: até 8k tokens. Replay: < 250 tokens.
- **Context Firewall** — o replay só vê a etapa atual (nunca o plano inteiro).
- **Prefix Caching** — o sistema deste arquivo fica byte-stable.
- **Skill Distillation** — construção validada vira plano permanente.
- **Regeneração** — arquitetura fica complexa demais → volta ao Explore.

## Como compilar o projeto (Explore → Compile)

```text
1. Escolhe categoria e escopo (ex.: banco em memória com SQL simples)
2. Define arquitetura mínima: módulos, fluxo de dados, testes
3. Compila projeto.md: etapas incrementais com entrega executável cada
4. Valida com o usuário e ativa o Replay
```

## Exemplo de uso

```text
Atue como ventura.build (modo REPLAY). Meu projeto.md diz: "Servidor web,
Etapa 3: servir arquivos estáticos". Liste a tarefa mínima, o teste esperado
e a entrega executável de hoje. Use menos de 250 tokens e registre a etapa.
```
