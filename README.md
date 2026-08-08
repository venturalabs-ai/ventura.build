# ventura.build

![Status](https://img.shields.io/badge/status-engineering%20platform-blueviolet)
![License](https://img.shields.io/github/license/venturalabs-ai/ventura.build)
![Stars](https://img.shields.io/github/stars/venturalabs-ai/ventura.build)

**Plataforma compartilhada de engenharia do ecossistema Ventura, com workflows reutilizáveis de higiene, segurança, SBOM e validação de skills, além de trilhas educacionais “build it yourself”.**

## Classificação

**Engineering Platform + Curation / Skill Repository.** Este repositório mantém o baseline compartilhado de segurança e governança consumido por outros repositórios Ventura e também organiza trilhas educacionais próprias.

O workflow reutilizável `.github/workflows/repo-standard.yml` é um **Repository Security Baseline**. Ele não substitui testes funcionais específicos de cada projeto e não deve, isoladamente, ser apresentado como evidência de que uma aplicação é production-grade.

## Baseline compartilhado

O baseline central executa, quando aplicável:

- higiene básica do repositório;
- validação estrutural de Agent Skills e manifestos de conectores;
- Trivy bloqueante para vulnerabilidades corrigíveis HIGH/CRITICAL;
- upload SARIF;
- geração e retenção de SBOM SPDX.

Projetos executáveis continuam responsáveis por seus próprios gates de lint, testes, coverage, integração, build, performance e outros controles específicos do domínio.

## Referência upstream

A parte educacional é inspirada por coleções públicas como `build-your-own-x`. Consulte projetos e tutoriais originais para conteúdo upstream e respeite suas licenças.

## Trilhas

- servidores e protocolos;
- bancos de dados;
- interpretadores e compiladores;
- shells e ferramentas CLI;
- controle de versão;
- frameworks;
- jogos e sistemas básicos.

## Método Ventura

`EXPLORE → COMPILE → REPLAY → REGENERATE`

Cada construção deve começar com uma versão mínima funcional, testes e etapas verificáveis.

## Boas práticas

- não copiar código upstream sem respeitar licença;
- documentar decisões próprias;
- comparar resultados com referências públicas;
- manter cada etapa executável;
- separar claramente baseline de repositório de quality gates específicos do produto.

## Licença

Consulte [LICENSE](LICENSE). Materiais externos mantêm suas próprias licenças.
