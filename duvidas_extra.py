# Perguntas adicionais (Contratos, Direito Civil e Direito de Família).
# Importado por content.py. Textos informativos; revisar antes de publicar.

ATUALIZADO = "novembro de 2026"

EXTRA = [
    # ------------------------------------------------------------ CONTRATOS
    {
        "slug": "assinatura-eletronica-contrato",
        "grupo": "contratos", "area": "contratos",
        "pergunta": "Assinatura eletrônica vale como assinatura de contrato?",
        "meta": "Contratos assinados eletronicamente são válidos. Veja os requisitos, os tipos de assinatura e os cuidados para que o documento tenha força de prova.",
        "resposta": "Sim. Contratos assinados eletronicamente são válidos, desde que as partes aceitem esse meio e seja possível comprovar quem assinou e que o documento não foi alterado.",
        "corpo": """
<h2>O que diz a lei</h2>
<ul>
<li>A <strong>Medida Provisória nº 2.200-2/2001</strong> reconhece a validade de documentos eletrônicos assinados com certificado digital ICP-Brasil e também de outros meios de comprovação de autoria e integridade, desde que aceitos pelas partes.</li>
<li>A <strong>Lei nº 14.063/2020</strong> classifica as assinaturas eletrônicas em simples, avançada e qualificada, conforme o grau de segurança na identificação do signatário.</li>
<li>O <strong>Código de Processo Civil</strong> (art. 784, § 4º) admite assinatura eletrônica em títulos executivos e dispensa a assinatura de testemunhas quando a integridade do documento é conferida por provedor de assinatura.</li>
</ul>
<h2>Quando é preciso mais cuidado</h2>
<p>Atos que exigem escritura pública, como a compra e venda de imóveis acima de 30 salários mínimos, precisam seguir a forma legal. Nesses casos, existem atos notariais eletrônicos, mas por meio dos cartórios.</p>
<h2>Boas práticas para dar segurança ao contrato</h2>
<ul>
<li>Use uma plataforma que registre data, horário, endereço de IP e a trilha de auditoria da assinatura.</li>
<li>Confira a identificação de cada signatário (e-mail, CPF, documento).</li>
<li>Inclua no contrato uma cláusula em que as partes reconhecem a validade da assinatura eletrônica.</li>
<li>Guarde o arquivo final e o relatório de assinaturas.</li>
<li>Se o contrato precisar de força executiva, avalie a assinatura de testemunhas ou o uso de assinatura de nível mais alto.</li>
</ul>
""",
    },
    {
        "slug": "encerrar-contrato-antes-do-prazo",
        "grupo": "contratos", "area": "contratos",
        "pergunta": "Posso encerrar um contrato antes do prazo? Haverá multa?",
        "meta": "Entenda quando é possível encerrar um contrato antes do fim: distrato, rescisão, denúncia, multa e as regras do Código Civil.",
        "resposta": "Depende do que o contrato prevê e do tipo de contrato. Em geral, encerrar antes do prazo sem previsão ou sem acordo pode gerar multa ou indenização, mas há situações em que o encerramento é permitido.",
        "corpo": """
<h2>Primeiro: leia o contrato</h2>
<p>A maioria dos contratos traz uma cláusula de rescisão, com aviso prévio e multa. Esse é o primeiro lugar onde procurar a resposta.</p>
<h2>Caminhos possíveis</h2>
<ul>
<li><strong>Distrato:</strong> as partes combinam o encerramento. Deve seguir a mesma forma exigida para o contrato (art. 472 do Código Civil) e é o caminho mais seguro.</li>
<li><strong>Resilição unilateral (denúncia):</strong> só é possível quando a lei ou o contrato permitem (art. 473). Contratos por prazo indeterminado costumam poder ser encerrados com aviso prévio razoável.</li>
<li><strong>Resolução por descumprimento:</strong> se a outra parte não cumpre o que prometeu, quem foi prejudicado pode pedir o fim do contrato, com indenização por perdas e danos (art. 475).</li>
</ul>
<h2>E a multa?</h2>
<p>A multa (cláusula penal) pode ser reduzida pelo juiz se for excessiva ou se o contrato já foi cumprido em parte (art. 413). Em relações de consumo, existem regras próprias, como o direito de arrependimento em 7 dias para compras feitas fora do estabelecimento (art. 49 do CDC).</p>
<h2>O que fazer na prática</h2>
<ol>
<li>Reúna o contrato, aditivos e as comunicações trocadas.</li>
<li>Avise a outra parte por escrito, respeitando o aviso prévio.</li>
<li>Tente formalizar um distrato com quitação mútua.</li>
<li>Em caso de impasse, avalie a notificação formal antes de qualquer ação.</li>
</ol>
""",
    },
    {
        "slug": "clausula-lgpd-contratos",
        "grupo": "contratos", "area": "contratos",
        "pergunta": "Preciso de cláusula de LGPD nos meus contratos?",
        "meta": "Contratos que envolvem dados pessoais devem prever regras de proteção de dados. Veja o que incluir e por que isso protege a sua empresa.",
        "resposta": "Sempre que o contrato envolver o tratamento de dados pessoais, é recomendável prever regras de proteção de dados. Isso define quem faz o quê com os dados e quem responde se algo der errado.",
        "corpo": """
<h2>Por que isso importa</h2>
<p>A LGPD distingue o <strong>controlador</strong> (quem decide como os dados serão usados) do <strong>operador</strong> (quem trata os dados em nome do controlador). Ambos podem responder por danos causados aos titulares (art. 42), e o operador deve seguir as instruções do controlador (art. 39). Um contrato sem essas regras deixa a empresa exposta.</p>
<h2>Exemplos comuns</h2>
<p>Contratos com contabilidade, software em nuvem, agências de marketing, clínicas, prestadores de RH e qualquer fornecedor que acesse dados de clientes ou empregados.</p>
<h2>O que costuma constar</h2>
<ul>
<li>Quais dados serão tratados e para qual finalidade.</li>
<li>Papel de cada parte (controlador ou operador).</li>
<li>Instruções de tratamento e proibição de uso para outros fins.</li>
<li>Medidas de segurança exigidas.</li>
<li>Regras para subcontratação de terceiros.</li>
<li>Comunicação de incidentes de segurança, com prazo.</li>
<li>Apoio para atender solicitações dos titulares.</li>
<li>Devolução ou eliminação dos dados ao final do contrato.</li>
<li>Regras de transferência internacional, quando houver.</li>
</ul>
<h2>Cuidado com cláusulas genéricas</h2>
<p>Um parágrafo padrão copiado de outro contrato raramente descreve o que realmente acontece com os dados. A cláusula deve refletir a operação real, e o nível de detalhe deve ser proporcional ao risco.</p>
""",
    },
    {
        "slug": "pejotizacao-risco-vinculo",
        "grupo": "contratos", "area": "contratos",
        "atualizado": True,
        "pergunta": "Contratar prestador como “PJ” tem risco de vínculo de emprego?",
        "meta": "Contratar profissional por pessoa jurídica é permitido, mas pode ser desconsiderado se houver vínculo de emprego na prática. Entenda o risco e o debate no STF.",
        "resposta": "Pode ter. Contratar profissional por meio de pessoa jurídica é permitido em muitas situações, mas, se na prática houver características de emprego, a Justiça do Trabalho pode reconhecer o vínculo, independentemente do que o contrato diz.",
        "corpo": """
<h2>O que pesa mais: a realidade, não o papel</h2>
<p>O vínculo de emprego depende de requisitos previstos na CLT (art. 3º): trabalho pessoal, não eventual, remunerado e com subordinação. Se esses requisitos existem na prática, o contrato de prestação de serviços pode ser desconsiderado, seguindo o princípio da primazia da realidade.</p>
<h2>Sinais que costumam gerar risco</h2>
<ul>
<li>Horário fixo e controle de jornada.</li>
<li>Ordens diretas e rotina igual à de um empregado.</li>
<li>Exclusividade e atuação como parte da equipe interna.</li>
<li>Pagamento fixo mensal, sem relação com entregas.</li>
<li>Impossibilidade de se fazer substituir ou de atender outros clientes.</li>
<li>Uso de e-mail, equipamentos e estrutura da empresa como se fosse empregado.</li>
</ul>
<h2>O que diz o STF</h2>
<p>O STF já considerou lícita a terceirização, inclusive de atividade-fim, quando não há fraude. Além disso, a Corte discute no <strong>Tema 1389</strong> a licitude da contratação de trabalhadores como pessoa jurídica ou autônomos, a competência da Justiça do Trabalho para analisar esses contratos e a quem cabe o ônus da prova. O julgamento ainda está em andamento e houve decisões sobre a suspensão e a retomada de processos. O cenário pode mudar.</p>
<h2>Como reduzir o risco</h2>
<ul>
<li>Contrato com escopo, entregas e prazos bem definidos.</li>
<li>Autonomia real na forma de executar o serviço.</li>
<li>Pagamento por serviço ou resultado, e não por jornada.</li>
<li>Prática do dia a dia compatível com o que está escrito.</li>
<li>Análise prévia da situação concreta, inclusive com advogado trabalhista, quando necessário.</li>
</ul>
""",
    },
    # ---------------------------------------------------------- DIREITO CIVIL
    {
        "slug": "golpe-do-pix-banco-devolve",
        "grupo": "civel", "area": "direito-civil",
        "atualizado": True,
        "pergunta": "Caí em golpe do Pix: o banco precisa devolver o dinheiro?",
        "meta": "Vítima de golpe do Pix? Veja o que fazer nas primeiras horas, quando o banco pode ser responsabilizado e como funciona o pedido de devolução.",
        "resposta": "Depende do caso. Os bancos respondem por fraudes em operações bancárias quando há falha no serviço, mas o STJ tem afastado essa responsabilidade quando não há falha do banco, por exemplo em transferências compatíveis com o perfil do cliente.",
        "corpo": """
<h2>O que fazer logo depois do golpe</h2>
<ol>
<li><strong>Acione o banco imediatamente</strong>, pelo aplicativo ou pela central, e peça a contestação da operação e o bloqueio dos valores. As regras do Banco Central preveem um mecanismo de devolução em casos de fraude, e o tempo faz diferença.</li>
<li><strong>Registre um boletim de ocorrência</strong>, de preferência online.</li>
<li><strong>Guarde todas as provas:</strong> conversas, números de telefone, comprovantes, prints de tela e protocolos de atendimento.</li>
<li><strong>Troque senhas</strong> e avise os contatos, se houve invasão de conta ou de WhatsApp.</li>
<li>Se o banco negar, registre reclamação no Banco Central, no consumidor.gov.br ou no Procon.</li>
</ol>
<h2>Quando o banco pode ser responsabilizado</h2>
<p>A Súmula 479 do STJ reconhece que as instituições financeiras respondem objetivamente por danos causados por fraudes de terceiros no âmbito de suas operações. Na prática, a responsabilidade costuma ser mais fácil de sustentar quando:</p>
<ul>
<li>a transação era fora do perfil do cliente (valor, horário, frequência ou destinatário) e o banco não bloqueou;</li>
<li>houve vazamento ou falha de segurança atribuível à instituição;</li>
<li>o banco demorou ou falhou em atender o pedido de bloqueio.</li>
</ul>
<h2>Quando costuma ser difícil</h2>
<p>Em casos em que a própria vítima, induzida por golpista, autoriza a transferência compatível com seu perfil, sem falha do banco, decisões recentes do STJ têm afastado o dever de indenizar. Cada caso depende de prova e da análise do histórico da conta.</p>
<h2>Cuidado com “golpe de recuperação”</h2>
<p>Desconfie de quem promete recuperar o dinheiro mediante pagamento antecipado. É comum que vítimas sejam golpeadas pela segunda vez.</p>
""",
    },
    {
        "slug": "negativacao-indevida-indenizacao",
        "grupo": "civel", "area": "direito-civil",
        "pergunta": "Meu nome foi negativado indevidamente. Tenho direito a indenização?",
        "meta": "Nome negativado por engano ou por dívida paga? Saiba quando cabe indenização por dano moral, o que diz o STJ e o que fazer.",
        "resposta": "Em regra, sim. A inscrição indevida em cadastro de inadimplentes gera dano moral presumido: não é preciso provar o sofrimento, apenas que a negativação foi indevida.",
        "corpo": """
<h2>Situações comuns de negativação indevida</h2>
<ul>
<li>Dívida que já foi paga e continua registrada (o credor deve providenciar a baixa em até 5 dias úteis após o pagamento, conforme a Súmula 548 do STJ).</li>
<li>Dívida que a pessoa nunca contratou (fraude ou erro).</li>
<li>Dívida prescrita.</li>
<li>Inscrição sem a comunicação prévia exigida pelo CDC (Súmula 359 do STJ).</li>
</ul>
<h2>Limite importante: a Súmula 385</h2>
<p>Se já existia outra negativação legítima anterior, a nova inscrição indevida em regra não gera indenização, embora possa ser cancelada. Por isso, antes de processar, vale conferir o seu histórico.</p>
<h2>Empresas também podem pedir</h2>
<p>A Súmula 227 do STJ reconhece que a pessoa jurídica também pode sofrer dano moral. Para empresas, o prejuízo costuma envolver crédito, fornecedores e reputação.</p>
<h2>O que fazer</h2>
<ol>
<li>Consulte seu CPF/CNPJ nos cadastros de proteção ao crédito e guarde os comprovantes.</li>
<li>Reúna provas do pagamento ou da inexistência da dívida.</li>
<li>Peça a exclusão ao credor por escrito e registre reclamação (consumidor.gov.br ou Procon).</li>
<li>Se não resolver, avalie ação judicial com pedido de exclusão imediata do registro e de indenização.</li>
</ol>
<p>O valor da indenização varia conforme o caso, e há prazo para ajuizar a ação, então não deixe a situação se arrastar.</p>
""",
    },
    {
        "slug": "divida-prescrita-cobranca",
        "grupo": "civel", "area": "direito-civil",
        "pergunta": "Dívida prescrita pode ser cobrada ou negativada?",
        "meta": "Dívida prescrita não pode mais ser cobrada na Justiça nem manter o nome negativado. Veja o que prescrição significa e os cuidados antes de pagar ou negociar.",
        "resposta": "A dívida prescrita não pode mais ser cobrada na Justiça, e o nome não pode ficar negativado por mais de cinco anos. Prescrita não significa que a dívida deixou de existir: o credor apenas perde o poder de exigi-la judicialmente.",
        "corpo": """
<h2>O que é prescrição</h2>
<p>É a perda do direito de exigir judicialmente uma obrigação depois de certo prazo (art. 189 do Código Civil). Para dívidas líquidas constantes de instrumento público ou particular, o prazo costuma ser de <strong>cinco anos</strong> (art. 206, § 5º, I), mas existem outros prazos conforme o tipo de dívida.</p>
<h2>E a negativação?</h2>
<p>Os cadastros não podem manter informações negativas por mais de cinco anos (art. 43, § 1º, do CDC e Súmula 323 do STJ). Se a prescrição se consumou, os órgãos de proteção ao crédito não podem fornecer informações que dificultem novo acesso ao crédito (art. 43, § 5º).</p>
<h2>Cobrança fora da Justiça</h2>
<p>O tema é discutido nos tribunais. De modo geral, cobranças que causem constrangimento, coação ou induzam o devedor a erro são consideradas abusivas.</p>
<h2>Cuidados antes de pagar ou negociar</h2>
<ul>
<li>Confira se o prazo realmente venceu, pois ele pode ter sido <strong>interrompido</strong> por ação judicial, protesto ou reconhecimento da dívida (art. 202).</li>
<li>Quem paga voluntariamente uma dívida prescrita não tem direito de pedir o dinheiro de volta (art. 882).</li>
<li>Um novo acordo pode criar uma nova obrigação, por isso avalie antes de assinar.</li>
</ul>
<h2>Para quem cobra</h2>
<p>Se você é credor, não deixe a dívida chegar ao prazo sem uma providência. Cobrança formal, protesto e ação judicial interrompem ou evitam a prescrição, e a hora de agir é antes.</p>
""",
    },
    {
        "slug": "juizado-especial-precisa-de-advogado",
        "grupo": "civel", "area": "direito-civil",
        "pergunta": "Preciso de advogado no Juizado Especial?",
        "meta": "No Juizado Especial Cível, advogado é dispensado em causas de até 20 salários mínimos. Veja limites, custos e quem pode ajuizar, inclusive microempresas.",
        "resposta": "Nas causas de até 20 salários mínimos, não é obrigatório. Entre 20 e 40 salários mínimos, a assistência de advogado é obrigatória (Lei nº 9.099/1995).",
        "corpo": """
<h2>O que o Juizado julga</h2>
<p>Causas cíveis de menor complexidade, com valor de até 40 salários mínimos, como cobranças, problemas de consumo, indenizações simples e outros conflitos do dia a dia. Em geral não há cobrança de custas no primeiro grau.</p>
<h2>Advogado: obrigatório ou não?</h2>
<ul>
<li><strong>Até 20 salários mínimos:</strong> a parte pode ir sozinha.</li>
<li><strong>De 20 a 40 salários mínimos:</strong> advogado é obrigatório.</li>
<li><strong>Para recorrer:</strong> o advogado é obrigatório, em qualquer valor.</li>
</ul>
<h2>O que o Juizado não julga</h2>
<p>Causas complexas, que dependam de perícia mais elaborada, e algumas matérias específicas, como alimentos, estado e capacidade das pessoas e assuntos fiscais (art. 3º, § 2º).</p>
<h2>Empresas podem usar o Juizado?</h2>
<p>Pessoas jurídicas em geral não podem ser autoras, mas <strong>microempresas e empresas de pequeno porte</strong> podem ajuizar ações no Juizado Especial Cível (art. 8º, § 1º). Todas as empresas podem ser rés.</p>
<h2>Mesmo quando não é obrigatório</h2>
<p>O advogado pode ajudar a organizar as provas, escolher o pedido correto e evitar erros que levem à perda da ação, como um valor acima do limite ou documentos insuficientes. Cada caso deve ser avaliado individualmente.</p>
""",
    },
    {
        "slug": "inquilino-nao-paga-despejo",
        "grupo": "civel", "area": "direito-civil",
        "pergunta": "O inquilino não paga o aluguel. Como funciona o despejo?",
        "meta": "Inquilino em atraso? Entenda a ação de despejo por falta de pagamento, a purga da mora, a liminar e o que o proprietário não pode fazer.",
        "resposta": "O proprietário pode ajuizar ação de despejo por falta de pagamento (Lei nº 8.245/1991). O inquilino pode evitar o despejo pagando a dívida em juízo, mas essa possibilidade só pode ser usada uma vez a cada 24 meses.",
        "corpo": """
<h2>Passo a passo</h2>
<ol>
<li><strong>Reúna os documentos:</strong> contrato, comprovantes de cobrança e planilha dos valores em atraso.</li>
<li><strong>Tente a solução amigável ou a notificação formal.</strong> Não é obrigatória, mas ajuda a comprovar a cobrança.</li>
<li><strong>Ação de despejo</strong>, que pode ser cumulada com a cobrança dos aluguéis e encargos.</li>
<li><strong>Citação do inquilino</strong>, que tem prazo para pagar tudo e evitar o despejo (purga da mora, art. 62), ou contestar.</li>
<li>Se não houver pagamento, o juiz determina a desocupação.</li>
</ol>
<h2>Liminar para desocupação</h2>
<p>Em algumas situações, como quando o contrato está sem garantia, o juiz pode conceder liminar para desocupação em 15 dias, mediante caução equivalente a três meses de aluguel (art. 59, § 1º, IX).</p>
<h2>E o fiador?</h2>
<p>O contrato de locação é título executivo extrajudicial (art. 784, VIII, do CPC). Havendo fiador, é possível cobrar também dele, conforme a garantia prevista.</p>
<h2>O que o proprietário não pode fazer</h2>
<ul>
<li>Cortar água ou luz.</li>
<li>Trocar a fechadura ou impedir a entrada do inquilino.</li>
<li>Retirar os bens do imóvel por conta própria.</li>
<li>Expor a dívida publicamente.</li>
</ul>
<p>Essas condutas podem gerar indenização contra o proprietário. A retomada deve ser feita pela via judicial.</p>
""",
    },
    # ------------------------------------------------------ DIREITO DE FAMÍLIA
    {
        "slug": "pix-pensao-alimenticia",
        "grupo": "familia", "area": "direito-de-familia",
        "atualizado": True,
        "pergunta": "O que é o “Pix Pensão” e como vai funcionar?",
        "meta": "Entenda o Pix Pensão (Lei 15.479/2026): débito automático da pensão alimentícia por ordem judicial, quando começa a valer e o que existe hoje para cobrar pensão.",
        "resposta": "É o nome popular da Lei nº 15.479/2026, que permite ao juiz determinar o débito automático da pensão alimentícia na conta do devedor, com repasse direto à conta de quem recebe. A lei foi sancionada em julho de 2026 e, segundo as notícias divulgadas, só passa a valer um ano depois.",
        "corpo": """
<h2>Como funcionará</h2>
<ul>
<li>O pedido é feito no processo de cobrança ou de execução da pensão.</li>
<li>Se o juiz aceitar, envia uma ordem eletrônica à instituição financeira do devedor.</li>
<li>O valor da pensão é debitado e repassado automaticamente a quem tem direito.</li>
<li>Diferentemente de um Pix agendado comum, o pagamento da pensão não poderia ser cancelado pelo devedor.</li>
</ul>
<p>O texto da lei fala em transferência automática, e não exige necessariamente o uso do Pix. A regulamentação operacional ainda deve ser detalhada, e entidades como o IBDFAM pediram ao CNJ uma regulamentação nacional.</p>
<h2>E até lá?</h2>
<p>Quem não recebe a pensão pode usar os mecanismos atuais:</p>
<ul>
<li><strong>Desconto em folha de pagamento</strong>, quando o devedor tem emprego formal.</li>
<li><strong>Penhora</strong> de bens e valores.</li>
<li><strong>Protesto</strong> da decisão judicial.</li>
<li><strong>Prisão civil</strong>, nos casos previstos em lei, para dívidas recentes (em regra, as três últimas prestações e as vencidas durante o processo).</li>
</ul>
<h2>Importante</h2>
<p>A pensão deve ser paga em dia, e o atraso pode gerar consequências sérias. Se a sua situação financeira mudou, o caminho correto é pedir a revisão do valor na Justiça, e não deixar de pagar.</p>
""",
    },
    {
        "slug": "como-calcular-pensao-alimenticia",
        "grupo": "familia", "area": "direito-de-familia",
        "pergunta": "Como é calculado o valor da pensão alimentícia?",
        "meta": "Não há percentual fixo em lei. Entenda o binômio necessidade e possibilidade, o que entra no cálculo, como pedir revisão e quando a pensão termina.",
        "resposta": "Não há porcentagem fixa em lei. O valor é definido por acordo ou pelo juiz, com base na necessidade de quem recebe e na possibilidade de quem paga (art. 1.694, § 1º, do Código Civil).",
        "corpo": """
<h2>O que se avalia</h2>
<ul>
<li><strong>Necessidades de quem recebe:</strong> moradia, alimentação, saúde, educação, vestuário e lazer.</li>
<li><strong>Possibilidades de quem paga:</strong> renda, patrimônio e outras obrigações, inclusive outros filhos.</li>
<li><strong>Contribuição de ambos os pais:</strong> a responsabilidade é dividida na proporção dos recursos de cada um (art. 1.703).</li>
</ul>
<h2>Como o valor é fixado</h2>
<p>É comum que a pensão seja definida em percentual dos rendimentos líquidos ou em valor fixo, por exemplo em salários mínimos. Cada decisão depende das provas apresentadas, e não existe um percentual padrão que sirva para todos os casos.</p>
<h2>O valor pode mudar?</h2>
<p>Sim. Se mudar a necessidade de quem recebe ou a possibilidade de quem paga, qualquer das partes pode pedir a revisão do valor (art. 1.699), por meio de ação revisional ou de novo acordo.</p>
<h2>Quando a pensão termina?</h2>
<p>A maioridade, por si só, não cancela a pensão automaticamente. Conforme a Súmula 358 do STJ, a exoneração depende de decisão judicial, com oportunidade de defesa, e é avaliada caso a caso (por exemplo, se o filho estuda ou tem condições de se sustentar).</p>
<h2>Mudanças em discussão</h2>
<p>Há projetos em tramitação no Congresso para estabelecer critérios mais objetivos de cálculo, mas eles ainda não são lei.</p>
""",
    },
    {
        "slug": "guarda-compartilhada-como-funciona",
        "grupo": "familia", "area": "direito-de-familia",
        "pergunta": "Como funciona a guarda compartilhada?",
        "meta": "Guarda compartilhada é a regra no Brasil. Veja o que significa, se o tempo é dividido igualmente, como fica a pensão e quando a guarda unilateral é possível.",
        "resposta": "Na guarda compartilhada, pai e mãe dividem as decisões importantes sobre a vida dos filhos e a responsabilidade por eles, mesmo morando em casas diferentes. É a regra no Brasil desde a Lei nº 13.058/2014, inclusive quando não há acordo entre os pais.",
        "corpo": """
<h2>O que significa na prática</h2>
<p>A guarda compartilhada significa responsabilização conjunta e exercício de direitos e deveres de ambos os pais sobre os filhos (art. 1.583, § 1º, do Código Civil). Decisões sobre educação, saúde e rotina devem ser tomadas em conjunto.</p>
<h2>O tempo precisa ser dividido igualmente?</h2>
<p>Não necessariamente. A lei fala em convívio equilibrado, e o tempo é organizado conforme a rotina da criança. Também é definida uma <strong>cidade-base</strong> de moradia, aquela que melhor atender aos interesses do filho (art. 1.583, § 3º).</p>
<h2>E a pensão alimentícia?</h2>
<p>A guarda compartilhada não elimina automaticamente a pensão. O valor continua sendo definido conforme as necessidades do filho e as possibilidades de cada um dos pais.</p>
<h2>Quando é possível a guarda unilateral?</h2>
<p>Quando um dos pais declara que não deseja a guarda ou quando há elementos que indiquem risco de violência doméstica ou familiar (art. 1.584, § 2º). O juiz sempre decide pensando no <strong>melhor interesse da criança</strong>.</p>
<h2>O pai ou a mãe sem a guarda perde direitos?</h2>
<p>Não. O poder familiar permanece com ambos, e o genitor sem a guarda mantém o direito de convivência e o dever de supervisionar os interesses dos filhos.</p>
<h2>Como organizar</h2>
<p>Um plano de convivência por escrito, com calendário de dias, feriados, férias e regras de comunicação, reduz conflitos. Ele pode ser homologado pela Justiça, o que dá mais segurança aos dois pais.</p>
""",
    },
    {
        "slug": "inventario-cartorio-ou-justica",
        "grupo": "familia", "area": "direito-de-familia",
        "pergunta": "Inventário: posso fazer em cartório ou preciso ir à Justiça?",
        "meta": "Inventário em cartório é possível quando todos os herdeiros são maiores, capazes e concordam. Veja requisitos, documentos, prazos e quando é preciso ir à Justiça.",
        "resposta": "Pode ser feito em cartório quando todos os herdeiros são maiores, capazes e estão de acordo, com a assistência de advogado. Havendo herdeiro menor ou incapaz, ou desacordo, o caminho costuma ser a Justiça.",
        "corpo": """
<h2>Inventário extrajudicial (em cartório)</h2>
<p>Previsto na Lei nº 11.441/2007 e no art. 610 do CPC, é feito por escritura pública. Os requisitos principais são:</p>
<ul>
<li>todos os herdeiros maiores e capazes;</li>
<li>concordância entre eles sobre a divisão dos bens;</li>
<li>assistência de advogado, que assina a escritura.</li>
</ul>
<p>Em regra, a existência de testamento ou de herdeiro menor ou incapaz leva ao inventário judicial, mas há situações em que a via do cartório é admitida. Isso depende do caso e das normas aplicáveis.</p>
<h2>Vantagens</h2>
<ul>
<li>Mais rápido do que o processo judicial.</li>
<li>Sem fila no Judiciário.</li>
<li>Custos de cartório que variam conforme o valor dos bens.</li>
</ul>
<h2>Documentos comuns</h2>
<ul>
<li>Certidão de óbito e documentos pessoais do falecido e dos herdeiros.</li>
<li>Certidões de casamento ou de união estável.</li>
<li>Documentos dos bens (imóveis, veículos, contas e participações).</li>
<li>Comprovante de pagamento do imposto sobre a herança (ITCMD).</li>
</ul>
<h2>Prazo</h2>
<p>O Código de Processo Civil prevê que o inventário seja aberto em até dois meses da morte e concluído em doze meses (art. 611). Alguns estados cobram multa sobre o imposto se o prazo for ultrapassado, por isso não vale a pena deixar o inventário parado.</p>
""",
    },
    {
        "slug": "holding-familiar-evita-inventario",
        "grupo": "familia", "area": "direito-de-familia",
        "atualizado": True,
        "pergunta": "Holding familiar evita o inventário?",
        "meta": "A holding familiar organiza a sucessão, mas não elimina automaticamente o inventário nem os impostos. Entenda como funciona, os limites e as alternativas.",
        "resposta": "Não automaticamente. A holding pode facilitar e organizar a sucessão, mas bens que continuam em nome da pessoa falecida ainda passam por inventário, e os impostos não desaparecem.",
        "corpo": """
<h2>O que é uma holding familiar</h2>
<p>É uma empresa criada para reunir o patrimônio da família, como imóveis e participações. Os bens passam a pertencer à empresa, e os familiares recebem quotas, o que pode simplificar a administração e a transmissão.</p>
<h2>O que ela pode ajudar a fazer</h2>
<ul>
<li>Organizar a gestão do patrimônio.</li>
<li>Planejar a transmissão das quotas em vida, por doação, com reserva de usufruto.</li>
<li>Estabelecer regras de governança entre os herdeiros.</li>
<li>Prever cláusulas restritivas, como inalienabilidade, impenhorabilidade e incomunicabilidade, observados os limites legais.</li>
</ul>
<h2>Limites e cuidados</h2>
<ul>
<li><strong>Inventário:</strong> o que continua em nome do falecido, inclusive quotas não doadas, ainda precisa ser inventariado.</li>
<li><strong>Herdeiros necessários:</strong> a lei protege a legítima, que corresponde à metade do patrimônio (art. 1.846). A doação que a ultrapassa pode ser contestada (art. 549).</li>
<li><strong>Credores:</strong> transferir bens para fugir de dívidas pode ser anulado como fraude contra credores (art. 158).</li>
<li><strong>Impostos:</strong> continuam existindo, como o ITCMD (estadual) na doação ou herança, e podem incidir ITBI e imposto de renda conforme a operação. Normas recentes mexeram nas regras do ITCMD, que depende da legislação de cada estado.</li>
<li><strong>Custos:</strong> constituição, contabilidade e manutenção da empresa.</li>
</ul>
<h2>Existem alternativas?</h2>
<p>Sim: testamento, doação com usufruto e previdência privada (VGBL e PGBL). O seguro de vida, em regra, é pago direto aos beneficiários e não entra no inventário (art. 794). A melhor escolha depende do patrimônio, da família e dos objetivos, e deve ser avaliada com advogado e contador.</p>
""",
    },
]
