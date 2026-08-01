# Encapsulamento
- protege o sistema contra interfência externa, mantedo-o íntegro
- o usuário deve utilizar o sistema sem a necessidade de entender como funciona e sem interferir em seu funcionamento
- apenas usuários autorizados podem ter acesso

## Vantagens
- segurança
- manutenção
- reutilização

## Como encapsular e manter a segurança
### Visibilidade
- publica   (+) --> pode ser alterado a qualquer momento no código principal
- protegido (#) --> pode ser alterado nas classes filhas mas não no código principal
- privado   (-) --> so pode ser alterado na classe mãe

> ### Consenting Adults
> O Python não protege rigidamente os dados  
> Foi feita uma covenção que determina o respeito à visibilidade dos dados, porém o desenvolvedor pode ignorá-la
> se quiser

### Visibilidade no Python
- publica   --> atributo_publico
- protegido --> _atributo_protegido
- privado   --> __atributo_privado