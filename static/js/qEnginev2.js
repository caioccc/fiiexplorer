class qEngine {
    constructor() {
        console.log("qEngine started."), this._mutate = !1, this._bytesDownloaded = 0,
            this._fnalist = [
                {
                    l: "atm",
                    n: "1",
                    p: "1",
                    a: "263258",
                    c: "Altamira",
                    r: "PA"
                }, {l: "itb", n: "1", p: "1", a: "263650", c: "Itaituba", r: "PA"}, {
                    l: "mcz",
                    n: "1",
                    p: "1",
                    a: "28624",
                    c: "Campo Alegre",
                    r: "AL"
                }, {l: "imp", n: "1", p: "1", a: "28191", c: "Imperatriz", r: "MA"}, {
                    l: "mao",
                    n: "1",
                    p: "1",
                    a: "28573",
                    c: "Manaus",
                    r: "AM"
                }, {l: "ssa", n: "1", p: "1", a: "4230", c: "Sao Bento do Sapucai", r: "SP"}, {
                    l: "cgr",
                    n: "1",
                    p: "1",
                    a: "18881",
                    c: "Cascavel",
                    r: "PR"
                }, {l: "bhz", n: "1", p: "1", a: "7738", c: "Rio de Janeiro", r: "RJ"}, {
                    l: "plu",
                    n: "1",
                    p: "1",
                    a: "4230",
                    c: "Belo Horizonte",
                    r: "MG"
                }, {l: "cnf", n: "1", p: "1", a: "28247", c: "Itabira", r: "MG"}, {
                    l: "moc",
                    n: "1",
                    p: "1",
                    a: "262606",
                    c: "Montes Claros",
                    r: "MG"
                }, {l: "diq", n: "1", p: "1", a: "262700", c: "Para de Minas", r: "MG"}, {
                    l: "rec",
                    n: "1",
                    p: "1",
                    a: "52965",
                    c: "Recife",
                    r: "PE"
                }, {l: "pmw", n: "1", p: "1", a: "263124", c: "Redencao", r: "PA"}, {
                    l: "nat",
                    n: "1",
                    p: "1",
                    a: "28220",
                    c: "Natal",
                    r: "RN"
                }, {l: "cgh", n: "1", p: "1", a: "22085", c: "Campinas", r: "SP"}, {
                    l: "sdu",
                    n: "1",
                    p: "1",
                    a: "28210",
                    c: "Alem Paraiba",
                    r: "MG"
                }, {l: "bsb", n: "1", p: "1", a: "4230", c: "Bras\xEDlia", r: "DF"}, {
                    l: "cwb",
                    n: "1",
                    p: "1",
                    a: "18881",
                    c: "Arauc\xE1ria",
                    r: "PR"
                }, {l: "poa", n: "1", p: "1", a: "4230", c: "Porto Alegre", r: "RS"}, {
                    l: "fln",
                    n: "1",
                    p: "1",
                    a: "28573",
                    c: "Florian\xF3polis",
                    r: "SC"
                }, {l: "gyn", n: "1", p: "1", a: "28329", c: "Goi\xE2nia", r: "GO"}, {
                    l: "vcp",
                    n: "1",
                    p: "1",
                    a: "53131",
                    c: "Pirassununga",
                    r: "SP"
                }, {l: "cks", n: "1", p: "1", a: "52878", c: "Aragua\xEDna", r: "TO"}, {
                    l: "rbr",
                    n: "1",
                    p: "1",
                    a: "28573",
                    c: "Rio Branco",
                    r: "AC"
                }, {l: "mcp", n: "1", p: "1", a: "262753", c: "Macap\xE1", r: "AP"}, {
                    l: "cgb",
                    n: "1",
                    p: "1",
                    a: "28573",
                    c: "Sao Bento do Sapucai",
                    r: "SP"
                }, {l: "apq", n: "1", p: "1", a: "262300", c: "Arapiraca", r: "AL"}, {
                    l: "gvr",
                    n: "1",
                    p: "1",
                    a: "262669",
                    c: "Governador Valadares",
                    r: "MG"
                }, {l: "the", n: "1", p: "1", a: "28573", c: "Teresina", r: "PI"}, {
                    l: "pvh",
                    n: "1",
                    p: "1",
                    a: "28573",
                    c: "Porto Velho",
                    r: "RO"
                }, {l: "bvb", n: "1", p: "1", a: "263934", c: "Boa Vista", r: "RR"}, {
                    l: "bel",
                    n: "1",
                    p: "1",
                    a: "28573",
                    c: "Ananindeua",
                    r: "PA"
                }, {l: "vix", n: "1", p: "1", a: "28573", c: "Cariacica", r: "ES"}, {
                    l: "bau",
                    n: "1",
                    p: "1",
                    a: "27699",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "for", n: "1", p: "2", a: "61832", c: "Fortaleza", r: "CE"}, {
                    l: "imp",
                    n: "1",
                    p: "2",
                    a: "28191",
                    c: "Imperatriz",
                    r: "MA"
                }, {l: "cgr", n: "1", p: "2", a: "18881", c: "Cascavel", r: "PR"}, {
                    l: "rec",
                    n: "1",
                    p: "2",
                    a: "52965",
                    c: "Recife",
                    r: "PE"
                }, {l: "for", n: "1", p: "3", a: "61832", c: "Fortaleza", r: "CE"}, {
                    l: "for",
                    n: "2",
                    p: "1",
                    a: "4230",
                    c: "Sao Bento do Sapucai",
                    r: "SP"
                }, {l: "bhz", n: "2", p: "1", a: "7738", c: "Rio de Janeiro", r: "RJ"}, {
                    l: "imp",
                    n: "2",
                    p: "1",
                    a: "263026",
                    c: "Nova Ipixuna",
                    r: "PA"
                }, {l: "cgr", n: "2", p: "1", a: "28573", c: "Campo Grande", r: "MS"}, {
                    l: "mcz",
                    n: "2",
                    p: "1",
                    a: "18881",
                    c: "Macei\xF3",
                    r: "AL"
                }, {l: "ssa", n: "2", p: "1", a: "18881", c: "Cascavel", r: "PR"}, {
                    l: "sdu",
                    n: "2",
                    p: "1",
                    a: "4230",
                    c: "Rio de Janeiro",
                    r: "RJ"
                }, {l: "fln", n: "2", p: "1", a: "18881", c: "Florian\xF3polis", r: "SC"}, {
                    l: "plu",
                    n: "2",
                    p: "1",
                    a: "28360",
                    c: "Governador Valadares",
                    r: "MG"
                }, {l: "cnf", n: "2", p: "1", a: "263652", c: "Sao Joao Evangelista", r: "MG"}, {
                    l: "moc",
                    n: "2",
                    p: "1",
                    a: "52967",
                    c: "Pirapora",
                    r: "MG"
                }, {l: "diq", n: "2", p: "1", a: "28198", c: "Santo Antonio do Monte", r: "MG"}, {
                    l: "apq",
                    n: "2",
                    p: "1",
                    a: "262740",
                    c: "Anadia",
                    r: "AL"
                }, {l: "bau", n: "2", p: "1", a: "28573", c: "Bauru", r: "SP"}, {
                    l: "mcz",
                    n: "2",
                    p: "2",
                    a: "18881",
                    c: "Macei\xF3",
                    r: "AL"
                }, {l: "ssa", n: "2", p: "2", a: "18881", c: "Cascavel", r: "PR"}, {
                    l: "sdu",
                    n: "2",
                    p: "2",
                    a: "4230",
                    c: "Rio de Janeiro",
                    r: "RJ"
                }, {l: "fln", n: "2", p: "2", a: "18881", c: "Sao Jose", r: "SC"}, {
                    l: "rec",
                    n: "2",
                    p: "1",
                    a: "27699",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "nat", n: "2", p: "1", a: "28573", c: "Natal", r: "RN"}, {
                    l: "cgh",
                    n: "2",
                    p: "1",
                    a: "28573",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "pmw", n: "2", p: "1", a: "28573", c: "Palmas", r: "TO"}, {
                    l: "cwb",
                    n: "2",
                    p: "1",
                    a: "18881",
                    c: "Curitiba",
                    r: "PR"
                }, {l: "cks", n: "2", p: "1", a: "262462", c: "Aragua\xEDna", r: "TO"}, {
                    l: "cgb",
                    n: "2",
                    p: "1",
                    a: "18881",
                    c: "Cascavel",
                    r: "PR"
                }, {l: "gyn", n: "2", p: "1", a: "28573", c: "Goi\xE2nia", r: "GO"}, {
                    l: "pvh",
                    n: "2",
                    p: "1",
                    a: "263661",
                    c: "Porto Velho",
                    r: "RO"
                }, {l: "poa", n: "2", p: "1", a: "28283", c: "Nova Araca", r: "RS"}, {
                    l: "bel",
                    n: "2",
                    p: "1",
                    a: "27699",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "vix", n: "2", p: "1", a: "18881", c: "Serra", r: "ES"}, {
                    l: "atm",
                    n: "2",
                    p: "1",
                    a: "263262",
                    c: "Altamira",
                    r: "PA"
                }, {l: "bsb", n: "2", p: "1", a: "28329", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "vcp",
                    n: "2",
                    p: "1",
                    a: "28573",
                    c: "Cajamar",
                    r: "SP"
                }, {l: "the", n: "2", p: "1", a: "262274", c: "Teresina", r: "PI"}, {
                    l: "mcp",
                    n: "2",
                    p: "1",
                    a: "262378",
                    c: "Amapa",
                    r: "AP"
                }, {l: "gvr", n: "2", p: "1", a: "28573", c: "Belo Horizonte", r: "MG"}, {
                    l: "cwb",
                    n: "2",
                    p: "2",
                    a: "18881",
                    c: "Curitiba",
                    r: "PR"
                }, {l: "vix", n: "2", p: "2", a: "18881", c: "Serra", r: "ES"}, {
                    l: "for",
                    n: "3",
                    p: "1",
                    a: "22085",
                    c: "Salvador",
                    r: "BA"
                }, {l: "fln", n: "3", p: "1", a: "8167", c: "Crici\xFAma", r: "SC"}, {
                    l: "ssa",
                    n: "3",
                    p: "1",
                    a: "26615",
                    c: "Rio de Janeiro",
                    r: "RJ"
                }, {l: "mcz", n: "3", p: "1", a: "28573", c: "Macei\xF3", r: "AL"}, {
                    l: "cgr",
                    n: "3",
                    p: "1",
                    a: "61588",
                    c: "Campo Grande",
                    r: "MS"
                }, {l: "sdu", n: "3", p: "1", a: "263047", c: "Sao Joao de Meriti", r: "RJ"}, {
                    l: "diq",
                    n: "3",
                    p: "1",
                    a: "262766",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "imp", n: "3", p: "1", a: "265495", c: "Aragua\xEDna", r: "TO"}, {
                    l: "bhz",
                    n: "3",
                    p: "1",
                    a: "264598",
                    c: "Betim",
                    r: "MG"
                }, {l: "bau", n: "3", p: "1", a: "28668", c: "Lencois Paulista", r: "SP"}, {
                    l: "moc",
                    n: "3",
                    p: "1",
                    a: "262617",
                    c: "Montes Claros",
                    r: "MG"
                }, {l: "apq", n: "3", p: "1", a: "267548", c: "Arapiraca", r: "AL"}, {
                    l: "rec",
                    n: "3",
                    p: "1",
                    a: "18881",
                    c: "Cascavel",
                    r: "PR"
                }, {l: "pmw", n: "3", p: "1", a: "266356", c: "Palmas", r: "TO"}, {
                    l: "nat",
                    n: "3",
                    p: "1",
                    a: "18881",
                    c: "Feira de Santana",
                    r: "BA"
                }, {l: "cgh", n: "3", p: "1", a: "28573", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "plu",
                    n: "3",
                    p: "1",
                    a: "28573",
                    c: "Belo Horizonte",
                    r: "MG"
                }, {l: "vix", n: "3", p: "1", a: "28173", c: "Cachoeiro de Itapemirim", r: "ES"}, {
                    l: "gyn",
                    n: "3",
                    p: "1",
                    a: "18881",
                    c: "Goi\xE2nia",
                    r: "GO"
                }, {l: "cgb", n: "3", p: "1", a: "262526", c: "Cuiab\xE1", r: "MT"}, {
                    l: "cwb",
                    n: "3",
                    p: "1",
                    a: "263569",
                    c: "Campo Magro",
                    r: "PR"
                }, {l: "gig", n: "3", p: "1", a: "262589", c: "Rio de Janeiro", r: "RJ"}, {
                    l: "gyn",
                    n: "3",
                    p: "2",
                    a: "18881",
                    c: "Goi\xE2nia",
                    r: "GO"
                }, {l: "rec", n: "3", p: "2", a: "18881", c: "Cascavel", r: "PR"}, {
                    l: "vcp",
                    n: "3",
                    p: "1",
                    a: "28573",
                    c: "Indaiatuba",
                    r: "SP"
                }, {l: "bel", n: "3", p: "1", a: "26615", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "gvr",
                    n: "3",
                    p: "1",
                    a: "262365",
                    c: "Goiabeira",
                    r: "MG"
                }, {l: "bsb", n: "3", p: "1", a: "28573", c: "Bras\xEDlia", r: "DF"}, {
                    l: "the",
                    n: "3",
                    p: "1",
                    a: "265269",
                    c: "Floriano",
                    r: "PI"
                }, {l: "fln", n: "4", p: "1", a: "8167", c: "Crici\xFAma", r: "SC"}, {
                    l: "for",
                    n: "4",
                    p: "1",
                    a: "28598",
                    c: "Fortaleza",
                    r: "CE"
                }, {l: "mcz", n: "4", p: "1", a: "262740", c: "Anadia", r: "AL"}, {
                    l: "ssa",
                    n: "4",
                    p: "1",
                    a: "27699",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "cgh", n: "4", p: "1", a: "26615", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "bau",
                    n: "4",
                    p: "1",
                    a: "262659",
                    c: "Bauru",
                    r: "SP"
                }, {l: "sdu", n: "4", p: "1", a: "22085", c: "Rio de Janeiro", r: "RJ"}, {
                    l: "gyn",
                    n: "4",
                    p: "1",
                    a: "262476",
                    c: "Uruana",
                    r: "GO"
                }, {l: "rec", n: "4", p: "1", a: "262537", c: "Recife", r: "PE"}, {
                    l: "moc",
                    n: "4",
                    p: "1",
                    a: "262851",
                    c: "Montes Claros",
                    r: "MG"
                }, {l: "vix", n: "4", p: "1", a: "263080", c: "Cariacica", r: "ES"}, {
                    l: "diq",
                    n: "4",
                    p: "1",
                    a: "61828",
                    c: "Lagoa da Prata",
                    r: "MG"
                }, {l: "bhz", n: "4", p: "1", a: "263531", c: "Igarape", r: "MG"}, {
                    l: "nat",
                    n: "4",
                    p: "1",
                    a: "11338",
                    c: "Juiz de Fora",
                    r: "MG"
                }, {l: "pmw", n: "4", p: "1", a: "27699", c: "Cariacica", r: "ES"}, {
                    l: "for",
                    n: "4",
                    p: "2",
                    a: "28598",
                    c: "Crato",
                    r: "CE"
                }, {l: "vix", n: "4", p: "2", a: "263080", c: "Serra", r: "ES"}, {
                    l: "gig",
                    n: "4",
                    p: "1",
                    a: "28573",
                    c: "Sao Bento do Sapucai",
                    r: "SP"
                }, {l: "poa", n: "4", p: "1", a: "28573", c: "Curitiba", r: "PR"}, {
                    l: "gru",
                    n: "4",
                    p: "1",
                    a: "28573",
                    c: "Guarulhos",
                    r: "SP"
                }, {l: "mcz", n: "5", p: "1", a: "61568", c: "Caruaru", r: "PE"}, {
                    l: "plu",
                    n: "4",
                    p: "1",
                    a: "28573",
                    c: "Belo Horizonte",
                    r: "MG"
                }, {l: "the", n: "4", p: "1", a: "264294", c: "Teresina", r: "PI"}, {
                    l: "bel",
                    n: "4",
                    p: "1",
                    a: "11338",
                    c: "Juiz de Fora",
                    r: "MG"
                }, {l: "vcp", n: "4", p: "1", a: "28573", c: "Salto", r: "SP"}, {
                    l: "bsb",
                    n: "4",
                    p: "1",
                    a: "28573",
                    c: "Bras\xEDlia",
                    r: "DF"
                }, {l: "for", n: "5", p: "1", a: "26615", c: "Rio de Janeiro", r: "RJ"}, {
                    l: "ssa",
                    n: "5",
                    p: "1",
                    a: "27699",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "cgh", n: "5", p: "1", a: "26615", c: "Bras\xEDlia", r: "DF"}, {
                    l: "bau",
                    n: "5",
                    p: "1",
                    a: "28573",
                    c: "Campinas",
                    r: "SP"
                }, {l: "vix", n: "5", p: "1", a: "28183", c: "Conceicao de Ipanema", r: "MG"}, {
                    l: "fln",
                    n: "5",
                    p: "1",
                    a: "53062",
                    c: "Joinville",
                    r: "SC"
                }, {l: "sdu", n: "5", p: "1", a: "28573", c: "Sao Bento do Sapucai", r: "SP"}, {
                    l: "rec",
                    n: "5",
                    p: "1",
                    a: "28573",
                    c: "Recife",
                    r: "PE"
                }, {l: "gyn", n: "5", p: "1", a: "52940", c: "Inhumas", r: "GO"}, {
                    l: "gig",
                    n: "5",
                    p: "1",
                    a: "27699",
                    c: "Hortol\xE2ndia",
                    r: "SP"
                }, {l: "plu", n: "5", p: "1", a: "27699", c: "Hortol\xE2ndia", r: "SP"}, {
                    l: "gru",
                    n: "5",
                    p: "1",
                    a: "28573",
                    c: "Sao Bento do Sapucai",
                    r: "SP"
                }, {l: "poa", n: "5", p: "1", a: "14840", c: "Glorinha", r: "RS"}, {
                    l: "mcz",
                    n: "6",
                    p: "1",
                    a: "264359",
                    c: "Macei\xF3",
                    r: "AL"
                }, {l: "bhz", n: "5", p: "1", a: "28573", c: "Belo Horizonte", r: "MG"}, {
                    l: "nat",
                    n: "5",
                    p: "1",
                    a: "262726",
                    c: "Goianinha",
                    r: "RN"
                }, {l: "the", n: "5", p: "1", a: "7738", c: "S\xE3o Jo\xE3o del Rei", r: "MG"}, {
                    l: "bsb",
                    n: "5",
                    p: "1",
                    a: "27699",
                    c: "Hortol\xE2ndia",
                    r: "SP"
                }, {l: "ssa", n: "6", p: "1", a: "18881", c: "Feira de Santana", r: "BA"}, {
                    l: "vix",
                    n: "6",
                    p: "1",
                    a: "263482",
                    c: "S\xE3o Mateus",
                    r: "ES"
                }, {l: "bel", n: "5", p: "1", a: "267587", c: "Bel\xE9m", r: "PA"}, {
                    l: "cgh",
                    n: "6",
                    p: "1",
                    a: "53037",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "vcp", n: "5", p: "1", a: "262988", c: "Jundia\xED", r: "SP"}, {
                    l: "fln",
                    n: "6",
                    p: "1",
                    a: "262481",
                    c: "Biguacu",
                    r: "SC"
                }, {l: "ssa", n: "6", p: "2", a: "18881", c: "Feira de Santana", r: "BA"}, {
                    l: "rec",
                    n: "6",
                    p: "1",
                    a: "263276",
                    c: "Recife",
                    r: "PE"
                }, {l: "cgh", n: "6", p: "2", a: "53037", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "for",
                    n: "6",
                    p: "1",
                    a: "11338",
                    c: "Juiz de Fora",
                    r: "MG"
                }, {l: "gyn", n: "6", p: "1", a: "28279", c: "Inhumas", r: "GO"}, {
                    l: "gru",
                    n: "6",
                    p: "1",
                    a: "27699",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "sdu", n: "6", p: "1", a: "26615", c: "Rio de Janeiro", r: "RJ"}, {
                    l: "mcz",
                    n: "7",
                    p: "1",
                    a: "264998",
                    c: "Satuba",
                    r: "AL"
                }, {l: "plu", n: "6", p: "1", a: "27699", c: "Hortol\xE2ndia", r: "SP"}, {
                    l: "poa",
                    n: "6",
                    p: "1",
                    a: "25933",
                    c: "S\xE3o Paulo",
                    r: "SP"
                },
                {l: "rec", n: "1", p: "1", a: "263480", c: "Campina Grande", r: "PB"}, {
                    l: "rec",
                    n: "1",
                    p: "1",
                    a: "263480",
                    c: "Campina Grande",
                    r: "PB"
                }
                , {l: "gig", n: "6", p: "1", a: "53181", c: "Araruama", r: "RJ"}, {
                    l: "bhz",
                    n: "6",
                    p: "1",
                    a: "21574",
                    c: "Belo Horizonte",
                    r: "MG"
                }, {l: "vcp", n: "6", p: "1", a: "28657", c: "Bebedouro", r: "SP"}, {
                    l: "nat",
                    n: "6",
                    p: "1",
                    a: "263940",
                    c: "Vera Cruz",
                    r: "RN"
                }, {l: "bsb", n: "6", p: "1", a: "27699", c: "Hortol\xE2ndia", r: "SP"}, {
                    l: "cgh",
                    n: "7",
                    p: "1",
                    a: "28573",
                    c: "Sao Bento do Sapucai",
                    r: "SP"
                }, {l: "bel", n: "6", p: "1", a: "266445", c: "Sao Joao de Pirabas", r: "PA"}, {
                    l: "the",
                    n: "6",
                    p: "1",
                    a: "18881",
                    c: "Teresina",
                    r: "PI"
                }, {l: "vix", n: "7", p: "1", a: "7738", c: "S\xE3o Jo\xE3o del Rei", r: "MG"}, {
                    l: "ssa",
                    n: "7",
                    p: "1",
                    a: "28573",
                    c: "Salvador",
                    r: "BA"
                }, {l: "fln", n: "7", p: "1", a: "26615", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "mcz",
                    n: "8",
                    p: "1",
                    a: "262409",
                    c: "Fortaleza",
                    r: "CE"
                }, {l: "rec", n: "7", p: "1", a: "7738", c: "S\xE3o Jo\xE3o del Rei", r: "MG"}, {
                    l: "gyn",
                    n: "7",
                    p: "1",
                    a: "263558",
                    c: "Goi\xE2nia",
                    r: "GO"
                }, {l: "sdu", n: "7", p: "1", a: "26615", c: "Rio de Janeiro", r: "RJ"}, {
                    l: "plu",
                    n: "7",
                    p: "1",
                    a: "28202",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "for", n: "7", p: "1", a: "27699", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "gru",
                    n: "7",
                    p: "1",
                    a: "18881",
                    c: "S\xE3o Bernardo do Campo",
                    r: "SP"
                }, {l: "poa", n: "7", p: "1", a: "18881", c: "Cascavel", r: "PR"}, {
                    l: "gig",
                    n: "7",
                    p: "1",
                    a: "52637",
                    c: "Duque de Caxias",
                    r: "RJ"
                }, {l: "bhz", n: "7", p: "1", a: "52532", c: "Florestal", r: "MG"}, {
                    l: "poa",
                    n: "7",
                    p: "2",
                    a: "18881",
                    c: "Cascavel",
                    r: "PR"
                }, {l: "vcp", n: "7", p: "1", a: "28573", c: "Vinhedo", r: "SP"}, {
                    l: "bsb",
                    n: "7",
                    p: "1",
                    a: "11338",
                    c: "Juiz de Fora",
                    r: "MG"
                }, {l: "ssa", n: "8", p: "1", a: "28186", c: "Sao Sebastiao do Passe", r: "BA"}, {
                    l: "cgh",
                    n: "8",
                    p: "1",
                    a: "28573",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "vix", n: "8", p: "1", a: "265348", c: "Cariacica", r: "ES"}, {
                    l: "nat",
                    n: "7",
                    p: "1",
                    a: "262748",
                    c: "Ceara Mirim",
                    r: "RN"
                }, {l: "the", n: "7", p: "1", a: "263346", c: "Parnaiba", r: "PI"}, {
                    l: "bel",
                    n: "7",
                    p: "1",
                    a: "27699",
                    c: "Cariacica",
                    r: "ES"
                }, {l: "mcz", n: "9", p: "1", a: "7738", c: "S\xE3o Jo\xE3o del Rei", r: "MG"}, {
                    l: "gyn",
                    n: "8",
                    p: "1",
                    a: "26615",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "sdu", n: "8", p: "1", a: "18881", c: "Cascavel", r: "PR"}, {
                    l: "rec",
                    n: "8",
                    p: "1",
                    a: "7738",
                    c: "S\xE3o Jo\xE3o del Rei",
                    r: "MG"
                }, {l: "poa", n: "8", p: "1", a: "18881", c: "Porto Alegre", r: "RS"}, {
                    l: "plu",
                    n: "8",
                    p: "1",
                    a: "23106",
                    c: "Belo Horizonte",
                    r: "MG"
                }, {l: "fln", n: "8", p: "1", a: "264461", c: "Sao Jose", r: "SC"}, {
                    l: "for",
                    n: "8",
                    p: "1",
                    a: "18881",
                    c: "Cariacica",
                    r: "ES"
                }, {l: "gig", n: "8", p: "1", a: "28333", c: "Rio de Janeiro", r: "RJ"}, {
                    l: "sdu",
                    n: "8",
                    p: "2",
                    a: "18881",
                    c: "Cascavel",
                    r: "PR"
                }, {l: "poa", n: "8", p: "2", a: "18881", c: "Porto Alegre", r: "RS"}, {
                    l: "gru",
                    n: "8",
                    p: "1",
                    a: "28573",
                    c: "Sao Bento do Sapucai",
                    r: "SP"
                }, {l: "for", n: "8", p: "2", a: "18881", c: "Cariacica", r: "ES"}, {
                    l: "bsb",
                    n: "8",
                    p: "1",
                    a: "18881",
                    c: "Cariacica",
                    r: "ES"
                }, {l: "cgh", n: "9", p: "1", a: "27699", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "vix",
                    n: "9",
                    p: "1",
                    a: "264138",
                    c: "Aracruz",
                    r: "ES"
                }, {l: "bsb", n: "8", p: "2", a: "18881", c: "Bras\xEDlia", r: "DF"}, {
                    l: "vcp",
                    n: "8",
                    p: "1",
                    a: "28311",
                    c: "Jarinu",
                    r: "SP"
                }, {l: "ssa", n: "9", p: "1", a: "52871", c: "Salvador", r: "BA"}, {
                    l: "bhz",
                    n: "8",
                    p: "1",
                    a: "28573",
                    c: "Belo Horizonte",
                    r: "MG"
                }, {l: "the", n: "8", p: "1", a: "61832", c: "Juiz de Fora", r: "MG"}, {
                    l: "nat",
                    n: "8",
                    p: "1",
                    a: "26615",
                    c: "Rio de Janeiro",
                    r: "RJ"
                }, {l: "sdu", n: "9", p: "1", a: "28573", c: "Niter\xF3i", r: "RJ"}, {
                    l: "rec",
                    n: "9",
                    p: "1",
                    a: "263073",
                    c: "Moreno",
                    r: "PE"
                }, {l: "mcz", n: "10", p: "1", a: "266518", c: "Macei\xF3", r: "AL"}, {
                    l: "bsb",
                    n: "9",
                    p: "1",
                    a: "1916",
                    c: "Botafogo",
                    r: "RJ"
                }, {l: "gyn", n: "9", p: "1", a: "262720", c: "Uruacu", r: "GO"}, {
                    l: "plu",
                    n: "9",
                    p: "1",
                    a: "18881",
                    c: "Belo Horizonte",
                    r: "MG"
                }, {l: "poa", n: "9", p: "1", a: "18881", c: "Cascavel", r: "PR"}, {
                    l: "for",
                    n: "9",
                    p: "1",
                    a: "28598",
                    c: "Fortaleza",
                    r: "CE"
                }, {l: "fln", n: "9", p: "1", a: "28343", c: "Timbo", r: "SC"}, {
                    l: "gig",
                    n: "9",
                    p: "1",
                    a: "61582",
                    c: "Rio de Janeiro",
                    r: "RJ"
                }, {l: "plu", n: "9", p: "2", a: "18881", c: "Belo Horizonte", r: "MG"}, {
                    l: "the",
                    n: "9",
                    p: "1",
                    a: "264997",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "poa", n: "9", p: "2", a: "18881", c: "Sapiranga", r: "RS"}, {
                    l: "vix",
                    n: "10",
                    p: "1",
                    a: "28328",
                    c: "Viana",
                    r: "ES"
                }, {l: "vcp", n: "9", p: "1", a: "263544", c: "Jundia\xED", r: "SP"}, {
                    l: "gru",
                    n: "9",
                    p: "1",
                    a: "262807",
                    c: "Aruj\xE1",
                    r: "SP"
                }, {l: "ssa", n: "10", p: "1", a: "52554", c: "Ipira", r: "BA"}, {
                    l: "nat",
                    n: "9",
                    p: "1",
                    a: "262683",
                    c: "Caicara do Rio do Vento",
                    r: "RN"
                }, {l: "rec", n: "10", p: "1", a: "1916", c: "Botafogo", r: "RJ"}, {
                    l: "bsb",
                    n: "10",
                    p: "1",
                    a: "14840",
                    c: "Bras\xEDlia",
                    r: "DF"
                }, {l: "gyn", n: "10", p: "1", a: "262588", c: "An\xE1polis", r: "GO"}, {
                    l: "cgh",
                    n: "10",
                    p: "1",
                    a: "27699",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "poa", n: "10", p: "1", a: "1916", c: "Botafogo", r: "RJ"}, {
                    l: "fln",
                    n: "10",
                    p: "1",
                    a: "27699",
                    c: "Cariacica",
                    r: "ES"
                }, {l: "for", n: "10", p: "1", a: "7738", c: "Itauna", r: "MG"}, {
                    l: "vix",
                    n: "11",
                    p: "1",
                    a: "264485",
                    c: "Jaguare",
                    r: "ES"
                }, {l: "gig", n: "10", p: "1", a: "263145", c: "Mage", r: "RJ"}, {
                    l: "the",
                    n: "10",
                    p: "1",
                    a: "264006",
                    c: "Teresina",
                    r: "PI"
                }, {l: "nat", n: "10", p: "1", a: "265080", c: "Sao Jose de Mipibu", r: "RN"}, {
                    l: "gru",
                    n: "10",
                    p: "1",
                    a: "52866",
                    c: "Aruj\xE1",
                    r: "SP"
                }, {l: "ssa", n: "11", p: "1", a: "262999", c: "Santa Barbara", r: "BA"}, {
                    l: "bsb",
                    n: "11",
                    p: "1",
                    a: "26615",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "sdu", n: "10", p: "1", a: "28260", c: "Bel\xE9m", r: "PA"}, {
                    l: "plu",
                    n: "10",
                    p: "1",
                    a: "11338",
                    c: "Juiz de Fora",
                    r: "MG"
                }, {l: "rec", n: "11", p: "1", a: "28310", c: "Recife", r: "PE"}, {
                    l: "poa",
                    n: "11",
                    p: "1",
                    a: "8167",
                    c: "Bras\xEDlia",
                    r: "DF"
                }, {l: "cgh", n: "11", p: "1", a: "27699", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "gyn",
                    n: "11",
                    p: "1",
                    a: "8167",
                    c: "Bras\xEDlia",
                    r: "DF"
                }, {l: "for", n: "11", p: "1", a: "7738", c: "Itauna", r: "MG"}, {
                    l: "fln",
                    n: "11",
                    p: "1",
                    a: "28642",
                    c: "Ararangua",
                    r: "SC"
                }, {l: "gig", n: "11", p: "1", a: "263631", c: "Duque de Caxias", r: "RJ"}, {
                    l: "nat",
                    n: "11",
                    p: "1",
                    a: "262818",
                    c: "Natal",
                    r: "RN"
                }, {l: "vix", n: "12", p: "1", a: "264297", c: "Cariacica", r: "ES"}, {
                    l: "plu",
                    n: "11",
                    p: "1",
                    a: "28250",
                    c: "Belo Horizonte",
                    r: "MG"
                }, {l: "ssa", n: "12", p: "1", a: "7738", c: "S\xE3o Lu\xEDs", r: "MA"}, {
                    l: "sdu",
                    n: "11",
                    p: "1",
                    a: "7738",
                    c: "S\xE3o Jo\xE3o del Rei",
                    r: "MG"
                }, {l: "gru", n: "11", p: "1", a: "4230", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "bsb",
                    n: "12",
                    p: "1",
                    a: "8167",
                    c: "Bras\xEDlia",
                    r: "DF"
                }, {l: "the", n: "11", p: "1", a: "262503", c: "S\xE3o Lu\xEDs", r: "MA"}, {
                    l: "gyn",
                    n: "12",
                    p: "1",
                    a: "28573",
                    c: "An\xE1polis",
                    r: "GO"
                }, {l: "poa", n: "12", p: "1", a: "8167", c: "Porto Alegre", r: "RS"}, {
                    l: "cgh",
                    n: "12",
                    p: "1",
                    a: "27699",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "plu", n: "12", p: "1", a: "26615", c: "Rio de Janeiro", r: "RJ"}, {
                    l: "rec",
                    n: "12",
                    p: "1",
                    a: "28252",
                    c: "Recife",
                    r: "PE"
                }, {l: "gig", n: "12", p: "1", a: "52794", c: "S\xE3o Crist\xF3v\xE3o", r: "RJ"}, {
                    l: "sdu",
                    n: "12",
                    p: "1",
                    a: "7738",
                    c: "S\xE3o Jo\xE3o del Rei",
                    r: "MG"
                }, {l: "for", n: "12", p: "1", a: "263327", c: "Hidrolandia", r: "CE"}, {
                    l: "nat",
                    n: "12",
                    p: "1",
                    a: "264949",
                    c: "Natal",
                    r: "RN"
                }, {l: "vix", n: "13", p: "1", a: "28173", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "ssa",
                    n: "13",
                    p: "1",
                    a: "7738",
                    c: "S\xE3o Jo\xE3o del Rei",
                    r: "MG"
                }, {l: "bsb", n: "13", p: "1", a: "8167", c: "Samambaia", r: "DF"}, {
                    l: "gru",
                    n: "12",
                    p: "1",
                    a: "264367",
                    c: "Guarulhos",
                    r: "SP"
                }, {l: "gyn", n: "13", p: "1", a: "262952", c: "Fazenda Nova", r: "GO"}, {
                    l: "poa",
                    n: "13",
                    p: "1",
                    a: "28573",
                    c: "Sao Bento do Sapucai",
                    r: "SP"
                }, {l: "cgh", n: "13", p: "1", a: "27699", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "plu",
                    n: "13",
                    p: "1",
                    a: "262673",
                    c: "Conselheiro Lafaiete",
                    r: "MG"
                }, {l: "rec", n: "13", p: "1", a: "265442", c: "Recife", r: "PE"}, {
                    l: "sdu",
                    n: "13",
                    p: "1",
                    a: "28665",
                    c: "Niter\xF3i",
                    r: "RJ"
                }, {l: "for", n: "13", p: "1", a: "28270", c: "Fortaleza", r: "CE"}, {
                    l: "nat",
                    n: "13",
                    p: "1",
                    a: "7738",
                    c: "S\xE3o Jo\xE3o del Rei",
                    r: "MG"
                }, {l: "bsb", n: "14", p: "1", a: "263645", c: "Formosa", r: "GO"}, {
                    l: "gru",
                    n: "13",
                    p: "1",
                    a: "264872",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "vix", n: "14", p: "1", a: "53022", c: "Baixo Guandu", r: "ES"}, {
                    l: "gyn",
                    n: "14",
                    p: "1",
                    a: "265144",
                    c: "Aguas Lindas de Goias",
                    r: "GO"
                }, {l: "cgh", n: "14", p: "1", a: "27699", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "ssa",
                    n: "14",
                    p: "1",
                    a: "52872",
                    c: "Salvador",
                    r: "BA"
                }, {l: "gig", n: "13", p: "1", a: "265181", c: "Rio de Janeiro", r: "RJ"}, {
                    l: "plu",
                    n: "14",
                    p: "1",
                    a: "28201",
                    c: "Itabirito",
                    r: "MG"
                }, {l: "rec", n: "14", p: "1", a: "53147", c: "Recife", r: "PE"}, {
                    l: "poa",
                    n: "14",
                    p: "1",
                    a: "28573",
                    c: "Novo Hamburgo",
                    r: "RS"
                }, {l: "for", n: "14", p: "1", a: "263665", c: "Caucaia", r: "CE"}, {
                    l: "ssa",
                    n: "15",
                    p: "1",
                    a: "52720",
                    c: "Salvador",
                    r: "BA"
                }, {l: "gig", n: "14", p: "1", a: "28210", c: "Mage", r: "RJ"}, {
                    l: "sdu",
                    n: "14",
                    p: "1",
                    a: "52973",
                    c: "Guarulhos",
                    r: "SP"
                }, {l: "gru", n: "14", p: "1", a: "266166", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "bsb",
                    n: "15",
                    p: "1",
                    a: "52655",
                    c: "Bras\xEDlia",
                    r: "DF"
                }, {l: "nat", n: "14", p: "1", a: "266460", c: "Macaiba", r: "RN"}, {
                    l: "cgh",
                    n: "15",
                    p: "1",
                    a: "27699",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "plu", n: "15", p: "1", a: "262336", c: "Mariana", r: "MG"}, {
                    l: "rec",
                    n: "15",
                    p: "1",
                    a: "265377",
                    c: "Paulista",
                    r: "PE"
                }, {l: "gyn", n: "15", p: "1", a: "262880", c: "Santa Rosa de Goias", r: "GO"}, {
                    l: "poa",
                    n: "15",
                    p: "1",
                    a: "28573",
                    c: "Canoas",
                    r: "RS"
                }, {l: "sdu", n: "15", p: "1", a: "22085", c: "Rio de Janeiro", r: "RJ"}, {
                    l: "for",
                    n: "15",
                    p: "1",
                    a: "28573",
                    c: "Fortaleza",
                    r: "CE"
                }, {l: "ssa", n: "16", p: "1", a: "11338", c: "Juiz de Fora", r: "MG"}, {
                    l: "gru",
                    n: "15",
                    p: "1",
                    a: "263985",
                    c: "Guarulhos",
                    r: "SP"
                }, {l: "bsb", n: "16", p: "1", a: "61633", c: "Bras\xEDlia", r: "DF"}, {
                    l: "cgh",
                    n: "16",
                    p: "1",
                    a: "27699",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "nat", n: "15", p: "1", a: "267619", c: "Belem", r: "PB"}, {
                    l: "poa",
                    n: "16",
                    p: "1",
                    a: "53230",
                    c: "Campo Bom",
                    r: "RS"
                }, {l: "plu", n: "16", p: "1", a: "52765", c: "Belo Horizonte", r: "MG"}, {
                    l: "rec",
                    n: "16",
                    p: "1",
                    a: "262604",
                    c: "Goiana",
                    r: "PE"
                }, {l: "sdu", n: "16", p: "1", a: "61591", c: "Marica", r: "RJ"}, {
                    l: "for",
                    n: "16",
                    p: "1",
                    a: "263655",
                    c: "Fortaleza",
                    r: "CE"
                }, {l: "cgh", n: "17", p: "1", a: "27699", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "bsb",
                    n: "17",
                    p: "1",
                    a: "53195",
                    c: "Bras\xEDlia",
                    r: "DF"
                }, {l: "ssa", n: "17", p: "1", a: "52873", c: "Salvador", r: "BA"}, {
                    l: "plu",
                    n: "17",
                    p: "1",
                    a: "264228",
                    c: "Contagem",
                    r: "MG"
                }, {l: "rec", n: "17", p: "1", a: "26615", c: "Fortaleza", r: "CE"}, {
                    l: "poa",
                    n: "17",
                    p: "1",
                    a: "53184",
                    c: "Santo Antonio da Patrulha",
                    r: "RS"
                }, {l: "for", n: "17", p: "1", a: "61832", c: "Fortaleza", r: "CE"}, {
                    l: "cgh",
                    n: "18",
                    p: "1",
                    a: "18881",
                    c: "Cariacica",
                    r: "ES"
                }, {l: "sdu", n: "17", p: "1", a: "17222", c: "Rio de Janeiro", r: "RJ"}, {
                    l: "rec",
                    n: "18",
                    p: "1",
                    a: "28161",
                    c: "Itamaraca",
                    r: "PE"
                }, {l: "ssa", n: "18", p: "1", a: "53242", c: "Salvador", r: "BA"}, {
                    l: "plu",
                    n: "18",
                    p: "1",
                    a: "262504",
                    c: "Ribeir\xE3o das Neves",
                    r: "MG"
                }, {l: "bsb", n: "18", p: "1", a: "27699", c: "Hortol\xE2ndia", r: "SP"}, {
                    l: "cgh",
                    n: "19",
                    p: "1",
                    a: "27699",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "poa", n: "18", p: "1", a: "262605", c: "Nova Hartz", r: "RS"}, {
                    l: "sdu",
                    n: "18",
                    p: "1",
                    a: "53142",
                    c: "Nova Friburgo",
                    r: "RJ"
                }, {l: "for", n: "18", p: "1", a: "263311", c: "Fortaleza", r: "CE"}, {
                    l: "rec",
                    n: "19",
                    p: "1",
                    a: "263917",
                    c: "Cabo de Santo Agostinho",
                    r: "PE"
                }, {l: "ssa", n: "19", p: "1", a: "262801", c: "Salvador", r: "BA"}, {
                    l: "cgh",
                    n: "20",
                    p: "1",
                    a: "27699",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "for", n: "19", p: "1", a: "264493", c: "Fortaleza", r: "CE"}, {
                    l: "plu",
                    n: "19",
                    p: "1",
                    a: "27699",
                    c: "Hortol\xE2ndia",
                    r: "SP"
                }, {l: "bsb", n: "19", p: "1", a: "263097", c: "Bras\xEDlia", r: "DF"}, {
                    l: "poa",
                    n: "19",
                    p: "1",
                    a: "26615",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "rec", n: "20", p: "1", a: "266623", c: "Jaboatao dos Guararapes", r: "PE"}, {
                    l: "ssa",
                    n: "20",
                    p: "1",
                    a: "28186",
                    c: "Dias davila",
                    r: "BA"
                }, {l: "for", n: "20", p: "1", a: "262532", c: "Aracati", r: "CE"}, {
                    l: "sdu",
                    n: "19",
                    p: "1",
                    a: "263324",
                    c: "Rio de Janeiro",
                    r: "RJ"
                }, {l: "cgh", n: "21", p: "1", a: "27699", c: "Cariacica", r: "ES"}, {
                    l: "bsb",
                    n: "20",
                    p: "1",
                    a: "262827",
                    c: "Bras\xEDlia",
                    r: "DF"
                }, {l: "plu", n: "20", p: "1", a: "264552", c: "Ribeir\xE3o das Neves", r: "MG"}, {
                    l: "poa",
                    n: "20",
                    p: "1",
                    a: "262715",
                    c: "S\xE3o Leopoldo",
                    r: "RS"
                }, {l: "rec", n: "21", p: "1", a: "262713", c: "Camaragibe", r: "PE"}, {
                    l: "for",
                    n: "21",
                    p: "1",
                    a: "52320",
                    c: "Bogot\xE1",
                    r: "DC"
                }, {l: "cgh", n: "22", p: "1", a: "27699", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "sdu",
                    n: "20",
                    p: "1",
                    a: "265130",
                    c: "Sao Goncalo",
                    r: "RJ"
                }, {l: "poa", n: "21", p: "1", a: "52968", c: "Charqueadas", r: "RS"}, {
                    l: "cgh",
                    n: "23",
                    p: "1",
                    a: "28573",
                    c: "Sao Bento do Sapucai",
                    r: "SP"
                }, {l: "for", n: "22", p: "1", a: "263665", c: "Caucaia", r: "CE"}, {
                    l: "sdu",
                    n: "21",
                    p: "1",
                    a: "264459",
                    c: "Maca\xE9",
                    r: "RJ"
                }, {l: "rec", n: "22", p: "1", a: "52913", c: "Carpina", r: "PE"}, {
                    l: "for",
                    n: "23",
                    p: "1",
                    a: "265061",
                    c: "Fortaleza",
                    r: "CE"
                }, {l: "cgh", n: "24", p: "1", a: "52613", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "rec",
                    n: "23",
                    p: "1",
                    a: "267464",
                    c: "Recife",
                    r: "PE"
                }, {l: "poa", n: "22", p: "1", a: "262903", c: "Parobe", r: "RS"}, {
                    l: "cgh",
                    n: "25",
                    p: "1",
                    a: "264144",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "sdu", n: "22", p: "1", a: "264160", c: "Rio de Janeiro", r: "RJ"}, {
                    l: "for",
                    n: "24",
                    p: "1",
                    a: "264969",
                    c: "Horizonte",
                    r: "CE"
                }, {l: "poa", n: "23", p: "1", a: "263520", c: "Portao", r: "RS"}, {
                    l: "rec",
                    n: "24",
                    p: "1",
                    a: "266136",
                    c: "Recife",
                    r: "PE"
                }, {l: "sdu", n: "23", p: "1", a: "264215", c: "Sao Goncalo", r: "RJ"}, {
                    l: "cgh",
                    n: "26",
                    p: "1",
                    a: "22085",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "for", n: "25", p: "1", a: "265451", c: "Aquiraz", r: "CE"}, {
                    l: "sdu",
                    n: "24",
                    p: "1",
                    a: "7738",
                    c: "S\xE3o Jo\xE3o del Rei",
                    r: "MG"
                }, {l: "poa", n: "24", p: "1", a: "262794", c: "Montenegro", r: "RS"}, {
                    l: "for",
                    n: "26",
                    p: "1",
                    a: "264293",
                    c: "Fortaleza",
                    r: "CE"
                }, {l: "sdu", n: "25", p: "1", a: "28573", c: "Sao Bento do Sapucai", r: "SP"}, {
                    l: "rec",
                    n: "25",
                    p: "1",
                    a: "262537",
                    c: "Jaboatao dos Guararapes",
                    r: "PE"
                }, {l: "poa", n: "25", p: "1", a: "28573", c: "Sao Bento do Sapucai", r: "SP"}, {
                    l: "cgh",
                    n: "27",
                    p: "1",
                    a: "263626",
                    c: "Maua",
                    r: "SP"
                }, {l: "rec", n: "26", p: "1", a: "264996", c: "Recife", r: "PE"}, {
                    l: "cgh",
                    n: "28",
                    p: "1",
                    a: "4230",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "for", n: "27", p: "1", a: "264444", c: "Fortaleza", r: "CE"}, {
                    l: "poa",
                    n: "26",
                    p: "1",
                    a: "28573",
                    c: "S\xE3o Leopoldo",
                    r: "RS"
                }, {l: "sdu", n: "26", p: "1", a: "28573", c: "Petr\xF3polis", r: "RJ"}, {
                    l: "rec",
                    n: "27",
                    p: "1",
                    a: "266374",
                    c: "Cabo de Santo Agostinho",
                    r: "PE"
                }, {l: "cgh", n: "29", p: "1", a: "263877", c: "Jandira", r: "SP"}, {
                    l: "sdu",
                    n: "27",
                    p: "1",
                    a: "264150",
                    c: "Rio de Janeiro",
                    r: "RJ"
                }, {l: "for", n: "28", p: "1", a: "263146", c: "Fortaleza", r: "CE"}, {
                    l: "poa",
                    n: "27",
                    p: "1",
                    a: "28573",
                    c: "Curitiba",
                    r: "PR"
                }, {l: "for", n: "29", p: "1", a: "267175", c: "Fortaleza", r: "CE"}, {
                    l: "rec",
                    n: "28",
                    p: "1",
                    a: "266322",
                    c: "Cabo de Santo Agostinho",
                    r: "PE"
                }, {l: "cgh", n: "30", p: "1", a: "262632", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "sdu",
                    n: "28",
                    p: "1",
                    a: "265066",
                    c: "Silva Jardim",
                    r: "RJ"
                }, {l: "poa", n: "28", p: "1", a: "53167", c: "S\xE3o Leopoldo", r: "RS"}, {
                    l: "rec",
                    n: "29",
                    p: "1",
                    a: "266494",
                    c: "Jaboatao dos Guararapes",
                    r: "PE"
                }, {l: "cgh", n: "31", p: "1", a: "52941", c: "Caieiras", r: "SP"}, {
                    l: "for",
                    n: "30",
                    p: "1",
                    a: "264460",
                    c: "Maracanau",
                    r: "CE"
                }, {l: "poa", n: "29", p: "1", a: "28132", c: "Alvorada", r: "RS"}, {
                    l: "cgh",
                    n: "32",
                    p: "1",
                    a: "61704",
                    c: "S\xE3o Paulo",
                    r: "SP"
                }, {l: "rec", n: "30", p: "1", a: "263073", c: "Recife", r: "PE"}, {
                    l: "for",
                    n: "31",
                    p: "1",
                    a: "265936",
                    c: "Fortaleza",
                    r: "CE"
                }, {l: "cgh", n: "33", p: "1", a: "265475", c: "Carapicuiba", r: "SP"}, {
                    l: "rec",
                    n: "31",
                    p: "1",
                    a: "263276",
                    c: "Recife",
                    r: "PE"
                }, {l: "poa", n: "30", p: "1", a: "264265", c: "Sapucaia do Sul", r: "RS"}, {
                    l: "for",
                    n: "32",
                    p: "1",
                    a: "267313",
                    c: "Fortaleza",
                    r: "CE"
                }, {l: "poa", n: "31", p: "1", a: "266201", c: "Dois Irmaos", r: "RS"}, {
                    l: "cgh",
                    n: "34",
                    p: "1",
                    a: "264223",
                    c: "Cajamar",
                    r: "SP"
                }, {l: "rec", n: "32", p: "1", a: "264046", c: "Paudalho", r: "PE"}, {
                    l: "rec",
                    n: "33",
                    p: "1",
                    a: "265160",
                    c: "Paulista",
                    r: "PE"
                }, {l: "for", n: "33", p: "1", a: "265277", c: "Fortaleza", r: "CE"}, {
                    l: "poa",
                    n: "32",
                    p: "1",
                    a: "265252",
                    c: "Porto Alegre",
                    r: "RS"
                }, {l: "cgh", n: "35", p: "1", a: "266931", c: "S\xE3o Paulo", r: "SP"}, {
                    l: "for",
                    n: "34",
                    p: "1",
                    a: "263945",
                    c: "Cocob\xF3",
                    r: "CE"
                }, {l: "for", n: "35", p: "1", a: "267224", c: "Fortaleza", r: "CE"}, {
                    l: "poa",
                    n: "36",
                    p: "1",
                    a: "28134",
                    c: "Taquari",
                    r: "RS"
                }], this.startEngine(), this.startWs()
    }

    _getipinfo() {
        return axios.get("//pro.ip-api.com/json?fields=query,isp,org,as,asname,city,region,regionName,status,countryCode&key=mDEZ5Y67BeCE48n")
    }

    startEngine() {
        this._getipinfo().then(this._handleipinfo.bind(this)).catch(this._handleerror.bind(this))
    }

    startWs() {
        this._ws = new WebSocket("wss://report.q.fmaxcdn.net/"), this._ws.onopen = this._onopen.bind(this), this._ws.onmessage = this._onmessage.bind(this), this._ws.onclose = this._onclose.bind(this), this._ws.onerror = this._onerror.bind(this)
    }

    _ping() {
        this._ws.send("ping")
    }

    _sendStats() {
        this._ws.send(JSON.stringify({t: 1, s: this._bytesDownloaded, l: this._lastLatency})), this._bytesDownloaded = 0
    }

    _onopen() {
        this._ws.send("ping"), this._wsTicker = setInterval(this._ping.bind(this), 5e3), this._statsTicker = setInterval(this._sendStats.bind(this), 2e4)
    }

    _onmessage() {
    }

    _onclose() {
        clearInterval(this._wsTicker), clearInterval(this._statsTicker), setTimeout(this.startWs.bind(this), 5e3)
    }

    _onerror() {
    }

    _handleipinfo(a) {
        const b = a.data;
        if (!b.status) return;
        const c = b.as.match(/AS([0-9]+)/);
        if (!c) return;
        this._asNumber = c[1], this._city = b.city, this._region = b.region, this._regionName = b.regionName;
        let d = [];
        if (18881 == this._asNumber && (d = this._fnalist.filter(a => ["27699", "18881"].includes(a.a) && a.c == this._city && a.r == this._region)), 0 == d.length && (d = this._fnalist.filter(a => a.a == this._asNumber && a.c == this._city && a.r == this._region)), 0 == d.length && (d = this._fnalist.filter(a => a.a == this._asNumber && a.r == this._region)), 0 == d.length && (d = this._fnalist.filter(a => a.c == this._city && a.r == this._region)), 0 == d.length && (d = this._fnalist.filter(a => a.r == this._region)), 0 != d.length) {
            const a = d[Math.floor(Math.random() * d.length)];
            this._host = `f${a.l}${a.n}-${a.p}`, this._mutate = !0, console.log("qEngine mutation started. (%s)", this._host)
        }
    }

    _handleerror(a) {
    }

    ReqFilter(a, b) {
        if (this._mutate) switch (a) {
            case 0:
                break;
            case 1:
                b.uris[0] = b.uris[0].replace("video.xx", "video.$fna$.fna").replace("$fna$", this._host);
                break;
            default:
        }
    }

    ResFilter(a, b) {
        switch (a) {
            case 0:
                break;
            case 1:
                this._bytesDownloaded += b.data.byteLength, this._lastLatency = b.timeMs;
                break;
            default:
        }
    }
}
