# Ventura Build Templates

Padrões reutilizáveis de containerização do ecossistema Ventura Labs AI.

## CPU

Use `templates/docker/Dockerfile.python` em serviços Python que precisem de imagem base enxuta, usuário não-root e healthcheck.

## NVIDIA GPU

Use `templates/gpu/Dockerfile.cuda` somente em workloads que realmente dependam de CUDA. O template parte de NVIDIA CUDA Runtime, expõe apenas `compute,utility` e executa a aplicação como usuário não-root.

Para Docker Compose, use `templates/gpu/docker-compose.gpu.yml`. O host precisa ter driver NVIDIA compatível e NVIDIA Container Toolkit instalado.

## Regra de arquitetura

GPU é **opt-in**, não padrão universal. Projetos web, documentação, APIs sem inferência local e serviços CPU-only não devem carregar CUDA apenas para cumprir padronização.

## Baseline comum

Todos os repositórios Ventura Labs AI apontam para `.github/workflows/repo-standard.yml`, que executa higiene de Git, Trivy, SARIF e geração de SBOM.
