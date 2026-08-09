# ventura.build

![Status](https://img.shields.io/badge/status-engineering%20platform-blueviolet)
![License](https://img.shields.io/github/license/venturalabs-ai/ventura.build)

**Plataforma compartilhada de engenharia e governança do ecossistema Ventura Labs AI.**

## Papel no ecossistema

`ventura.build` centraliza controles reutilizáveis para evitar que cada repositório replique lógica de segurança, CI, release e autonomia.

A plataforma distingue explicitamente:

- **Repository Security Baseline** — higiene, integridade, Actions, Skills, conectores, Trivy e SBOM;
- **Autonomy Gate** — política de execução, refs imutáveis e rejeição de testes meramente decorativos;
- **Curation Health** — proveniência e freshness de links para repositórios curatoriais;
- **Release Standard** — evidência de release SemVer, SBOM e checksums;
- **Failure Issue Template** — criação/deduplicação automática de Issues quando workflows falham.

Nenhum baseline compartilhado substitui testes funcionais específicos do domínio.

## Workflows reutilizáveis

### Repository Security Baseline

`.github/workflows/repo-standard.yml`

Executa, quando aplicável:

- higiene e integridade estrutural;
- auditoria de GitHub Actions;
- validação de Agent Skills e manifestos de conectores;
- Trivy bloqueante para vulnerabilidades corrigíveis HIGH/CRITICAL;
- SARIF;
- SBOM SPDX.

### Ventura Autonomy Gate

`.github/workflows/autonomy-gate.yml`

Adiciona controles para agentes autônomos:

- proíbe referências mutáveis de Actions/reusable workflows;
- rejeita o scaffold de teste estrutural que não prova comportamento;
- exige README/licença e `git diff --check`;
- pode executar o comando de testes Python do consumidor.

### Autonomous Failure Issue

`templates/ci-failure-issue.yml`

Template para cada repositório criar ou atualizar uma única Issue de falha de CI por workflow, evitando spam e transformando falhas em backlog operacional rastreável.

## Princípios de autonomia

1. **tool-first** — ferramenta determinística antes de LLM;
2. **least privilege** — permissões mínimas por workflow;
3. **immutable supply chain** — Actions pinadas por SHA completa;
4. **functional evidence** — teste deve provar comportamento relevante;
5. **fail closed** — erro de segurança ou validação bloqueia promoção;
6. **deduplicated feedback** — falhas viram Issues atualizáveis, não ruído;
7. **budget-aware agents** — custo e tokens pertencem ao control plane do `ventura.system`;
8. **no fictitious required checks** — somente checks existentes e verdes devem virar proteção obrigatória.

## Curadoria e proveniência

A parte educacional continua inspirada por coleções públicas como `build-your-own-x`. Materiais externos mantêm suas próprias licenças; o repositório deve registrar proveniência e não reproduzir conteúdo protegido sem permissão.

## Método Ventura

`EXPLORE → COMPILE → CONSTRAINED REPLAY → REGENERATE`

Caminhos validados devem virar workflows, testes ou Skills reutilizáveis; mudanças reais de requisito ou evidência acionam nova exploração.

## Licença

Consulte [LICENSE](LICENSE).
