# Textos do site. Edite aqui e rode `python3 build.py` para regenerar.
# Conteúdo em HTML simples (<p>, <ul>, <strong>...).

GRUPOS = [
    ("lgpd", "LGPD e proteção de dados"),
    ("contratos", "Contratos"),
    ("civel", "Direito Civil e cobrança"),
    ("familia", "Direito de Família"),
]

AREAS = [
    {
        "slug": "lgpd-e-protecao-de-dados",
        "titulo": "LGPD e Proteção de Dados",
        "icone": "dados",
        "resumo": "Adequação à LGPD, políticas de privacidade, contratos com fornecedores e atuação como encarregado (DPO).",
        "chamada": "Adequação à LGPD que cabe na rotina e no porte da sua empresa.",
        "meta": "Advogado em Vila Velha/ES para adequação à LGPD: mapeamento de dados, política de privacidade, contratos, DPO e resposta a incidentes.",
        "intro": "<p>A Lei Geral de Proteção de Dados (Lei nº 13.709/2018) se aplica a qualquer empresa que trate dados pessoais de clientes, empregados, fornecedores ou usuários, inclusive pequenos negócios. O meu trabalho é traduzir a lei para a operação real: entender como os dados circulam na empresa, identificar riscos e organizar documentos e processos de forma proporcional ao seu porte.</p><p>Além da formação jurídica, tenho formação em tecnologia e em análise de dados, o que facilita o diálogo com equipes de TI e a compreensão dos sistemas por trás dos documentos.</p>",
        "itens": [
            "<strong>Diagnóstico e mapeamento de dados:</strong> onde os dados pessoais são coletados, armazenados, compartilhados e descartados.",
            "<strong>Política de Privacidade, Termos de Uso e avisos</strong> adequados ao seu site, aplicativo ou atendimento.",
            "<strong>Bases legais e consentimento:</strong> definição da base adequada para cada tratamento.",
            "<strong>Contratos e cláusulas de proteção de dados</strong> com fornecedores, operadores e parceiros.",
            "<strong>Registro das operações e Relatório de Impacto (RIPD),</strong> quando necessário.",
            "<strong>Canal e fluxo para atender titulares</strong> e solicitações de direitos.",
            "<strong>Plano de resposta a incidentes</strong> de segurança e vazamentos.",
            "<strong>Encarregado (DPO) terceirizado</strong> e treinamento de equipes.",
        ],
        "publico": "Empresas de qualquer porte, startups, comércio eletrônico, clínicas, escritórios, condomínios, prestadores de serviço e todo negócio que lida com dados de clientes ou colaboradores.",
        "passos": [
            ("Conversa inicial.", "Entendo a sua atividade, os tipos de dados e as principais preocupações."),
            ("Diagnóstico.", "Levantamento de como os dados são tratados hoje e dos pontos de atenção."),
            ("Plano de adequação.", "Priorização do que precisa ser feito, em linguagem prática e com cronograma."),
            ("Implementação e acompanhamento.", "Elaboração de documentos, orientação à equipe e revisões periódicas."),
        ],
        "nota": "Cada empresa tem um nível diferente de exposição. A adequação é um processo contínuo e proporcional ao porte e ao tipo de dado tratado, e não existe garantia de ausência de incidentes ou de fiscalização.",
        "duvidas": ["lgpd-adequar-empresa", "penalidades-lgpd", "encarregado-dpo", "politica-de-privacidade-site", "vazamento-de-dados"],
    },
    {
        "slug": "contratos",
        "titulo": "Contratos",
        "icone": "contrato",
        "resumo": "Elaboração, revisão e análise de contratos empresariais e civis, com atenção a riscos e cláusulas.",
        "chamada": "Contratos claros previnem conflitos e protegem o que foi combinado.",
        "meta": "Elaboração e revisão de contratos em Vila Velha/ES: prestação de serviços, compra e venda, locação, acordo de sócios e contratos digitais.",
        "intro": "<p>Um bom contrato é a forma mais econômica de evitar problemas. Elaboro e reviso contratos de acordo com a realidade do negócio, deixando claro o que cada parte deve fazer, em quanto tempo e o que acontece se algo não sair como o esperado.</p>",
        "itens": [
            "Elaboração de contratos sob medida.",
            "Revisão e análise de riscos e cláusulas desfavoráveis antes da assinatura.",
            "Contratos de prestação de serviços e de parceria.",
            "Compra e venda, locação residencial e comercial.",
            "Acordo de sócios e alterações societárias.",
            "Termos de uso e contratos digitais.",
            "Aditivos, distratos e notificações.",
        ],
        "publico": "Empresários, profissionais autônomos, prestadores de serviço e pessoas físicas que vão assinar ou propor um contrato e querem segurança sobre o que estão assumindo.",
        "passos": [
            ("Entendimento do negócio.", "Quem são as partes, o que será entregue e quais as condições combinadas."),
            ("Elaboração ou revisão.", "Texto objetivo, com destaque para pontos de atenção."),
            ("Ajustes.", "Alterações até que o documento reflita o acordo real."),
            ("Orientação para assinatura.", "Formalização por assinatura física ou eletrônica."),
        ],
        "nota": "",
        "duvidas": ["contrato-verbal", "o-que-nao-pode-faltar-em-um-contrato"],
    },
    {
        "slug": "direito-civil",
        "titulo": "Direito Civil",
        "icone": "civil",
        "resumo": "Cobrança, responsabilidade civil, obrigações e demais conflitos patrimoniais, na esfera extrajudicial e judicial.",
        "chamada": "Orientação segura para resolver conflitos patrimoniais, dentro e fora do Judiciário.",
        "meta": "Advocacia cível em Vila Velha/ES: cobrança, responsabilidade civil, indenizações, locação e demais questões patrimoniais.",
        "intro": "<p>Atuo em questões cíveis do dia a dia de pessoas e empresas, priorizando, sempre que possível, soluções negociadas e extrajudiciais, e preparando o caso com cuidado quando o processo é inevitável.</p>",
        "itens": [
            "Cobrança e recuperação de crédito (extrajudicial e judicial).",
            "Responsabilidade civil e reparação de danos.",
            "Obrigações e inadimplemento contratual.",
            "Questões de locação.",
            "Direito do consumidor.",
            "Posse, propriedade e relações de vizinhança.",
            "Acompanhamento de processos e atuação consultiva.",
        ],
        "publico": "Pessoas físicas e empresas que precisam cobrar valores, defender-se em um conflito ou entender seus direitos e riscos antes de tomar uma decisão.",
        "passos": [
            ("Análise do caso.", "Avaliação dos documentos e das provas disponíveis."),
            ("Estratégia.", "Apresentação das alternativas (negociação, notificação, protesto ou ação) com seus prós e contras."),
            ("Atuação.", "Condução da solução escolhida, mantendo você informado em cada etapa."),
        ],
        "nota": "",
        "duvidas": ["cliente-nao-pagou"],
    },
    {
        "slug": "direito-de-familia",
        "titulo": "Direito de Família",
        "icone": "familia",
        "resumo": "Divórcio, união estável, guarda, pensão alimentícia e partilha, com atendimento sigiloso e acolhedor.",
        "chamada": "Atendimento reservado e objetivo para momentos delicados.",
        "meta": "Advogado de família em Vila Velha/ES: divórcio, união estável, guarda, pensão alimentícia, partilha de bens e inventário.",
        "intro": "<p>Questões familiares envolvem emoções e decisões importantes. O atendimento é feito com sigilo, linguagem clara e foco em soluções consensuais sempre que possível, o que costuma ser mais rápido e menos desgastante.</p>",
        "itens": [
            "Divórcio consensual e litigioso.",
            "Reconhecimento e dissolução de união estável; contrato de convivência.",
            "Guarda e convivência dos filhos.",
            "Pensão alimentícia: fixação, revisão e execução.",
            "Partilha de bens.",
            "Inventário e partilha de herança.",
        ],
        "publico": "Pessoas e famílias que precisam formalizar, reorganizar ou encerrar uma relação, ou resolver questões de filhos, bens e herança.",
        "passos": [
            ("Conversa reservada.", "Escuta do cenário e dos objetivos, com total sigilo."),
            ("Caminho adequado.", "Definição entre via extrajudicial (cartório) ou judicial."),
            ("Condução do processo.", "Elaboração de documentos, negociação e acompanhamento até a conclusão."),
        ],
        "nota": "",
        "duvidas": ["divorcio-em-cartorio", "uniao-estavel-precisa-registrar"],
    },
]

DUVIDAS = [
    {
        "slug": "lgpd-adequar-empresa",
        "grupo": "lgpd", "area": "lgpd-e-protecao-de-dados",
        "pergunta": "Minha empresa precisa se adequar à LGPD?",
        "meta": "Toda empresa que trata dados pessoais precisa cumprir a LGPD, mesmo as pequenas. Entenda o que a lei exige e o que significa se adequar.",
        "resposta": "Na grande maioria dos casos, sim. A LGPD se aplica a qualquer pessoa ou empresa que trate dados pessoais, independentemente do porte ou do setor.",
        "corpo": """
<h2>O que são dados pessoais</h2>
<p>É qualquer informação que identifique ou possa identificar uma pessoa: nome, CPF, e-mail, telefone, endereço, foto, dados de saúde, dados bancários e até o endereço IP. Se a sua empresa mantém cadastro de clientes, contrata empregados, atende por WhatsApp, usa câmeras ou tem um site com formulário, ela trata dados pessoais.</p>
<h2>Existem exceções?</h2>
<p>Sim, mas são restritas (art. 4º da LGPD): uso particular sem fins econômicos, fins exclusivamente jornalísticos, artísticos ou acadêmicos e atividades de segurança pública, entre outras. Atividades empresariais, em regra, estão dentro da lei.</p>
<h2>E as pequenas empresas?</h2>
<p>A Autoridade Nacional de Proteção de Dados (ANPD) criou regras simplificadas para agentes de tratamento de pequeno porte (Resolução CD/ANPD nº 2/2022), que flexibilizam algumas obrigações. Isso <strong>não isenta</strong> o negócio de cumprir a lei.</p>
<h2>O que significa “se adequar”</h2>
<ul>
<li>Mapear quais dados são tratados, para qual finalidade e com quem são compartilhados.</li>
<li>Definir a base legal adequada para cada tratamento.</li>
<li>Ter política de privacidade e avisos claros para os titulares.</li>
<li>Adotar medidas de segurança proporcionais ao risco.</li>
<li>Ter um canal para atender solicitações dos titulares.</li>
<li>Ajustar contratos com fornecedores que acessam dados.</li>
</ul>
""",
    },
    {
        "slug": "penalidades-lgpd",
        "grupo": "lgpd", "area": "lgpd-e-protecao-de-dados",
        "pergunta": "Quais são as penalidades previstas na LGPD?",
        "meta": "Veja quais sanções a LGPD prevê: advertência, multa de até 2% do faturamento (limitada a R$ 50 milhões por infração) e outras.",
        "resposta": "A LGPD prevê desde advertência até multa de até 2% do faturamento da empresa, limitada a R$ 50 milhões por infração, além de outras sanções que podem afetar a atividade.",
        "corpo": """
<h2>Sanções administrativas (art. 52)</h2>
<p>Aplicadas pela ANPD, desde agosto de 2021:</p>
<ul>
<li>Advertência, com prazo para adoção de medidas corretivas.</li>
<li>Multa simples de até 2% do faturamento da empresa no último exercício (excluídos tributos), limitada a R$ 50 milhões por infração.</li>
<li>Multa diária, observado o mesmo limite.</li>
<li>Publicização da infração.</li>
<li>Bloqueio e eliminação dos dados pessoais relacionados à infração.</li>
<li>Suspensão parcial do funcionamento do banco de dados ou do exercício da atividade de tratamento.</li>
<li>Proibição parcial ou total de atividades relacionadas a tratamento de dados.</li>
</ul>
<h2>A multa não é o único risco</h2>
<ul>
<li><strong>Ações judiciais</strong> de titulares por indenização, individuais ou coletivas (art. 42), inclusive por Ministério Público e órgãos de defesa do consumidor.</li>
<li><strong>Danos à reputação</strong> e perda de confiança de clientes.</li>
<li><strong>Exigências contratuais:</strong> empresas maiores têm exigido conformidade com a LGPD de seus fornecedores.</li>
</ul>
<h2>Como a sanção é definida</h2>
<p>A ANPD considera a gravidade da infração, a boa-fé, a cooperação, a reincidência e as medidas adotadas pela empresa, como a existência de programa de governança e a rapidez na correção. Por isso, estar organizado antes de qualquer problema faz diferença.</p>
""",
    },
    {
        "slug": "encarregado-dpo",
        "grupo": "lgpd", "area": "lgpd-e-protecao-de-dados",
        "pergunta": "O que é o encarregado (DPO) e minha empresa precisa ter um?",
        "meta": "Entenda o que faz o encarregado de dados (DPO), quando ele é obrigatório e a dispensa prevista para pequenos agentes de tratamento.",
        "resposta": "O encarregado, conhecido como DPO, é a pessoa indicada pela empresa como canal de comunicação com os titulares dos dados e com a ANPD. Em regra deve ser indicado, mas agentes de tratamento de pequeno porte podem ser dispensados.",
        "corpo": """
<h2>O que o encarregado faz (art. 41)</h2>
<ul>
<li>Recebe reclamações e pedidos dos titulares e presta esclarecimentos.</li>
<li>Recebe comunicações da ANPD e adota providências.</li>
<li>Orienta funcionários e contratados sobre boas práticas de proteção de dados.</li>
<li>Executa outras atribuições definidas pela empresa ou por normas complementares.</li>
</ul>
<p>A identidade e o contato do encarregado devem ser divulgados publicamente, de forma clara e objetiva, preferencialmente no site da empresa.</p>
<h2>E se a empresa for pequena?</h2>
<p>A Resolução CD/ANPD nº 2/2022 dispensa os agentes de tratamento de pequeno porte da obrigação de indicar um encarregado, mas eles devem manter um canal de comunicação para atender os titulares. A dispensa não vale em todas as situações (por exemplo, em tratamentos de alto risco), e a indicação voluntária é considerada uma boa prática.</p>
<h2>Quem pode ser o encarregado?</h2>
<p>Não é preciso ser advogado ou ter formação específica, mas é necessário conhecimento da lei e de segurança da informação. O encarregado pode ser interno ou terceirizado (o chamado “DPO como serviço”). Convém evitar que a função seja acumulada com cargos que decidam sobre a finalidade do tratamento dos dados, para prevenir conflitos de interesse.</p>
""",
    },
    {
        "slug": "politica-de-privacidade-site",
        "grupo": "lgpd", "area": "lgpd-e-protecao-de-dados",
        "pergunta": "Meu site precisa ter Política de Privacidade?",
        "meta": "Se o seu site coleta dados pessoais (formulários, cadastro, cookies de análise), a LGPD exige informações claras. Veja o que a política deve conter.",
        "resposta": "Sim, se o site coletar qualquer dado pessoal (formulário de contato, cadastro, cookies de análise ou publicidade). A LGPD garante ao titular informação clara e acessível sobre como seus dados são tratados.",
        "corpo": """
<h2>O que a política deve informar</h2>
<ul>
<li>Quem é o responsável pelo tratamento e como contatá-lo (incluindo o encarregado, quando houver).</li>
<li>Quais dados são coletados e para quais finalidades.</li>
<li>Qual a base legal de cada tratamento.</li>
<li>Com quem os dados são compartilhados.</li>
<li>Por quanto tempo são mantidos.</li>
<li>Quais os direitos do titular (art. 18) e como exercê-los.</li>
<li>Quais medidas de segurança são adotadas.</li>
</ul>
<h2>E os cookies?</h2>
<p>Cookies que não sejam estritamente necessários ao funcionamento do site, como os de análise e de publicidade, em geral exigem informação clara e, conforme o caso, consentimento do usuário. A ANPD publicou um guia orientativo sobre o tema.</p>
<h2>Cuidado com modelos prontos</h2>
<p>Copiar a política de outro site costuma ser um erro: o documento precisa refletir o que a <strong>sua</strong> empresa realmente faz com os dados. Uma política que diz uma coisa e uma operação que faz outra pode gerar mais risco do que não ter política.</p>
""",
    },
    {
        "slug": "vazamento-de-dados",
        "grupo": "lgpd", "area": "lgpd-e-protecao-de-dados",
        "pergunta": "O que fazer em caso de vazamento de dados?",
        "meta": "Houve vazamento de dados na sua empresa? Veja os primeiros passos, quando comunicar a ANPD e os titulares e como se preparar.",
        "resposta": "Agir rápido: conter o incidente, avaliar o risco e, se houver risco ou dano relevante aos titulares, comunicar a ANPD e as pessoas afetadas (art. 48). Pela regulamentação da ANPD, o prazo de comunicação é, em regra, de três dias úteis.",
        "corpo": """
<h2>Primeiros passos</h2>
<ol>
<li><strong>Conter o incidente:</strong> interromper o acesso indevido, trocar senhas e isolar sistemas afetados.</li>
<li><strong>Preservar evidências:</strong> registros de acesso e logs ajudam a entender o que ocorreu.</li>
<li><strong>Acionar o responsável:</strong> encarregado, TI e a assessoria jurídica.</li>
<li><strong>Avaliar o risco:</strong> que dados foram expostos, quantas pessoas foram afetadas e qual a probabilidade de dano.</li>
<li><strong>Comunicar:</strong> se houver risco ou dano relevante, informar a ANPD e os titulares afetados, em linguagem clara.</li>
<li><strong>Registrar:</strong> documentar o incidente e as medidas adotadas, mesmo quando não for necessário comunicar.</li>
<li><strong>Corrigir:</strong> revisar processos e controles para evitar repetição.</li>
</ol>
<h2>Prevenção</h2>
<p>O melhor momento para se preparar é antes do problema. Um <strong>plano de resposta a incidentes</strong>, com responsáveis definidos e modelos de comunicação, economiza tempo precioso. Medidas simples, como autenticação em duas etapas, controle de acessos e backups, reduzem muito a chance e o impacto de um vazamento.</p>
""",
    },
    {
        "slug": "contrato-verbal",
        "grupo": "contratos", "area": "contratos",
        "pergunta": "Contrato verbal tem validade?",
        "meta": "Contrato verbal vale? Em regra sim, mas é difícil de provar. Entenda as exceções e por que registrar por escrito protege você.",
        "resposta": "Em regra, sim. O Código Civil adota a liberdade de forma (art. 107): se a lei não exigir forma específica, o acordo é válido mesmo sem estar escrito. O problema costuma ser provar o que foi combinado.",
        "corpo": """
<h2>Quando a lei exige forma específica</h2>
<ul>
<li>Compra e venda de imóveis acima de 30 salários mínimos exige escritura pública (art. 108).</li>
<li>A fiança deve ser dada por escrito (art. 819).</li>
<li>Outros contratos têm exigências próprias de forma ou registro.</li>
</ul>
<h2>O risco do “combinado”</h2>
<p>Sem documento, cada parte tende a lembrar as condições de um jeito. É possível provar um acordo verbal por mensagens, e-mails, comprovantes de pagamento e testemunhas, mas isso costuma ser mais incerto e trabalhoso.</p>
<h2>Por que escrever</h2>
<ul>
<li>Deixa claro preço, prazo e responsabilidades.</li>
<li>Facilita a prova em caso de conflito.</li>
<li>Pode servir de <strong>título executivo extrajudicial</strong> quando assinado pelo devedor e por duas testemunhas (art. 784, III, do CPC), o que agiliza uma eventual cobrança.</li>
<li>Pode ser assinado de forma eletrônica, sem necessidade de imprimir.</li>
</ul>
""",
    },
    {
        "slug": "o-que-nao-pode-faltar-em-um-contrato",
        "grupo": "contratos", "area": "contratos",
        "pergunta": "O que não pode faltar em um contrato?",
        "meta": "Conheça as cláusulas essenciais de um contrato: partes, objeto, preço, prazo, rescisão, multa, proteção de dados e foro.",
        "resposta": "Um bom contrato deixa claro quem são as partes, o que foi combinado, quanto custa, por quanto tempo vale e o que acontece se algo der errado.",
        "corpo": """
<h2>Elementos essenciais</h2>
<ul>
<li><strong>Identificação das partes:</strong> nome completo ou razão social, CPF/CNPJ, endereço e quem representa cada parte.</li>
<li><strong>Objeto:</strong> o que será feito, vendido ou entregue, descrito de forma específica.</li>
<li><strong>Preço e forma de pagamento:</strong> valor, datas, reajuste e meios de pagamento.</li>
<li><strong>Prazo e vigência:</strong> início, término e regras de renovação.</li>
<li><strong>Obrigações de cada parte.</strong></li>
<li><strong>Multa, juros e consequências do descumprimento.</strong></li>
<li><strong>Rescisão:</strong> como e em que condições o contrato pode ser encerrado.</li>
<li><strong>Confidencialidade,</strong> quando houver troca de informações sensíveis.</li>
<li><strong>Proteção de dados pessoais,</strong> quando houver tratamento de dados.</li>
<li><strong>Foro:</strong> onde eventuais conflitos serão discutidos.</li>
<li><strong>Assinatura</strong> das partes e, se possível, de duas testemunhas.</li>
</ul>
<h2>Cuidado com modelos genéricos</h2>
<p>Modelos prontos podem conter cláusulas inadequadas ou abusivas para o seu caso e deixar de tratar de pontos importantes. Antes de assinar, vale revisar o texto com atenção, especialmente prazos, multas e condições de saída.</p>
""",
    },
    {
        "slug": "cliente-nao-pagou",
        "grupo": "civel", "area": "direito-civil",
        "pergunta": "Um cliente não me pagou. O que posso fazer?",
        "meta": "Cliente não pagou? Veja o passo a passo: reunir provas, cobrança amigável, protesto, execução e ação monitória, e os prazos de prescrição.",
        "resposta": "O caminho depende das provas que você tem da dívida, mas normalmente começa por uma cobrança amigável e documentada, antes de qualquer medida judicial.",
        "corpo": """
<h2>Passo a passo</h2>
<ol>
<li><strong>Reúna as provas:</strong> contrato, orçamento aprovado, nota fiscal, comprovante de entrega ou de execução do serviço, boletos e mensagens.</li>
<li><strong>Cobre de forma amigável e registrada:</strong> por e-mail ou mensagem, e, se necessário, por notificação extrajudicial.</li>
<li><strong>Negocie e formalize:</strong> um acordo escrito, com confissão de dívida assinada por duas testemunhas, pode ser título executivo extrajudicial.</li>
<li><strong>Protesto em cartório</strong> (Lei nº 9.492/1997): comprova a falta de pagamento e costuma estimular a regularização.</li>
<li><strong>Medida judicial:</strong> <em>execução</em>, se houver título executivo; <em>ação monitória</em>, se houver prova escrita sem força de título; ou <em>ação de cobrança</em>.</li>
</ol>
<h2>Atenção ao prazo</h2>
<p>A pretensão de cobrar dívidas líquidas constantes de instrumento público ou particular prescreve, em regra, em <strong>cinco anos</strong> (art. 206, § 5º, I, do Código Civil). Outros prazos podem se aplicar, conforme a natureza da dívida.</p>
<h2>O que evitar</h2>
<p>Cobranças vexatórias, ameaças ou exposição do devedor podem gerar responsabilidade e indenização contra quem cobra. A cobrança deve ser firme, mas respeitosa e documentada.</p>
""",
    },
    {
        "slug": "divorcio-em-cartorio",
        "grupo": "familia", "area": "direito-de-familia",
        "pergunta": "É possível fazer divórcio em cartório?",
        "meta": "Divórcio em cartório é possível quando é consensual e não há filhos menores ou incapazes. Veja requisitos, vantagens e quando é preciso ir à Justiça.",
        "resposta": "Sim. O divórcio consensual pode ser feito em cartório, por escritura pública, desde que o casal esteja de acordo e, em regra, não haja filhos menores de idade ou incapazes. As partes devem ser assistidas por advogado.",
        "corpo": """
<h2>Requisitos principais</h2>
<ul>
<li>Acordo entre os cônjuges sobre o divórcio e seus efeitos (Lei nº 11.441/2007 e art. 733 do CPC).</li>
<li>Em regra, ausência de filhos menores ou incapazes e de gravidez em curso. Nos casos com filhos, as normas locais e a situação concreta devem ser analisadas.</li>
<li>Assistência de advogado, que assina a escritura.</li>
</ul>
<h2>Não há prazo mínimo</h2>
<p>Desde a Emenda Constitucional nº 66/2010 não é preciso aguardar tempo de separação nem discutir culpa para se divorciar.</p>
<h2>O que normalmente se define</h2>
<ul>
<li>Partilha dos bens (ou a decisão de partilhar depois).</li>
<li>Uso do sobrenome de casado.</li>
<li>Pensão entre os cônjuges, quando for o caso.</li>
</ul>
<h2>Quando é preciso ir à Justiça</h2>
<p>Quando não há acordo (divórcio litigioso) ou quando há filhos menores ou incapazes e as regras aplicáveis exigem intervenção judicial. A via de cartório costuma ser mais rápida e simples, mas só deve ser escolhida após uma análise cuidadosa dos termos do acordo.</p>
""",
    },
    {
        "slug": "uniao-estavel-precisa-registrar",
        "grupo": "familia", "area": "direito-de-familia",
        "pergunta": "Preciso registrar a união estável?",
        "meta": "Registrar a união estável não é obrigatório, mas ajuda na prova e evita conflitos. Entenda regime de bens, escritura e direitos.",
        "resposta": "Não é obrigatório. A união estável existe pela convivência pública, contínua e duradoura com o objetivo de constituir família (art. 1.723 do Código Civil). Mas formalizá-la por escrito facilita a prova e evita conflitos.",
        "corpo": """
<h2>Como formalizar</h2>
<ul>
<li><strong>Escritura pública</strong> em cartório de notas.</li>
<li><strong>Contrato particular</strong> de convivência, assinado pelo casal.</li>
<li><strong>Registro</strong> no Livro E do Cartório de Registro Civil, que dá publicidade à união.</li>
</ul>
<h2>Regime de bens</h2>
<p>Sem contrato, aplica-se, em regra, o regime da <strong>comunhão parcial de bens</strong> (art. 1.725), ou seja, os bens adquiridos onerosamente durante a união são, em geral, divididos entre o casal. É possível escolher outro regime por contrato.</p>
<h2>Por que formalizar</h2>
<ul>
<li>Comprova o início da união e o regime de bens.</li>
<li>Facilita o acesso a plano de saúde, benefícios previdenciários e outros direitos.</li>
<li>Evita discussões em caso de separação ou falecimento.</li>
</ul>
<p>Em 2017, o Supremo Tribunal Federal equiparou os direitos sucessórios do companheiro aos do cônjuge, o que torna a organização patrimonial ainda mais relevante.</p>
""",
    },
]

# --- Página Sobre ---
# Texto em primeira pessoa, baseado no perfil do LinkedIn. Ajuste livremente.
SOBRE_PARAGRAFOS = [
    "Sou advogado desde 2016, com atuação em Direito Civil e Empresarial. Hoje, meu foco principal é a proteção de dados e a conformidade com a LGPD.",
    "Sempre tive interesse por tecnologia. Esse interesse me levou a estudar análise de dados e, depois, a cursar Análise e Desenvolvimento de Sistemas. Foi assim que percebi o quanto as empresas dependem de dados e o quanto isso cria responsabilidades jurídicas. Quando a LGPD entrou em vigor, encontrei o ponto de encontro entre as duas áreas de que mais gosto.",
    "Essa formação dupla me permite ir além de redigir contratos e políticas de privacidade: consigo compreender como os sistemas funcionam, mapear o caminho dos dados dentro da empresa e alinhar a segurança da informação às exigências legais.",
    "Meu trabalho é traduzir a lei para a rotina do negócio, de forma proporcional e prática, para reduzir riscos e manter a empresa em conformidade sem travar a operação.",
    "Atuo também em contratos, direito civil e direito de família, sempre com atendimento reservado e linguagem clara.",
]

FORMACAO = [
    ("Pós-graduado em Lei Geral de Proteção de Dados", "Legale Educacional · 2025–2026"),
    ("Graduado em Análise e Desenvolvimento de Sistemas", "Gran Cursos Online · 2023–2025"),
    ("Pós-graduado em Direito Civil e Processual Civil", "Legale Educacional · 2021–2022"),
    ("Bacharelado em Direito", "Universidade Vila Velha (UVV) · 2011–2015"),
    ("Certificado Profissional de Análise de Dados", "Google"),
    ("Compliance e Proteção de Dados · Introdução à LGPD", "Certificações complementares"),
]
