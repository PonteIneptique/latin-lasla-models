Confusion tables
================

# Index

- [Lemma](#lemma)
- [Part-Of-Speech](#pos)
- [Voice](#voice)
- [Mood](#mood)
- [Degree](#degree)
- [Numb](#number)
- [Person](#person)
- [Tense](#tense)
- [Case](#case)
- [Gender](#gender)

# Lemma

[Back to index](#index)

```
all:
  accuracy: 0.9773
  precision: 0.8485
  recall: 0.8438
  support: 170166
ambiguous-tokens:
  accuracy: 0.9308
  precision: 0.7199
  recall: 0.7229
  support: 39038
unknown-targets:
  accuracy: 0.6183
  precision: 0.4522
  recall: 0.4481
  support: 799
unknown-tokens:
  accuracy: 0.8824
  precision: 0.7503
  recall: 0.7458
  support: 5916
```

| Expected        | Total Errors | Predictions      | Predicted times |
|-----------------|--------------|------------------|-----------------|
| qui             | 243          | quod             | 88              |
|                 |              | quis             | 82              |
|                 |              | quam             | 31              |
|                 |              | quo              | 27              |
|                 |              | qua              | 14              |
|                 |              | antequam         | 1               |
| quis            | 160          | qui              | 153             |
|                 |              | quam             | 4               |
|                 |              | qua              | 1               |
|                 |              | quod             | 1               |
|                 |              | quo              | 1               |
| quod            | 95           | qui              | 95              |
| multus          | 39           | multi            | 20              |
|                 |              | multum           | 19              |
| sui             | 27           | suus             | 27              |
| multum          | 22           | multus           | 22              |
| quam            | 20           | qui              | 18              |
|                 |              | quis             | 1               |
|                 |              | priusquam        | 1               |
| tantus          | 17           | tantum           | 15              |
|                 |              | tanto            | 2               |
| suus            | 17           | sui              | 13              |
|                 |              | suum             | 4               |
| bonus           | 17           | bonum            | 16              |
|                 |              | bene             | 1               |
| quo             | 17           | qui              | 16              |
|                 |              | quis             | 1               |
| is              | 16           | eo               | 16              |
| boni            | 16           | bonum            | 8               |
|                 |              | bonus            | 8               |
| paruus          | 16           | parum            | 13              |
|                 |              | minimum          | 2               |
|                 |              | paruum           | 1               |
| multi           | 15           | multus           | 15              |
| bonum           | 15           | bonus            | 9               |
|                 |              | boni             | 6               |
| eo              | 15           | is               | 15              |
| facio           | 14           | factum           | 12              |
|                 |              | fax              | 1               |
|                 |              | facies           | 1               |
| antequam        | 13           | quam             | 10              |
|                 |              | qui              | 2               |
|                 |              | priusquam        | 1               |
| superus         | 13           | summa            | 8               |
|                 |              | summum           | 3               |
|                 |              | superi           | 2               |
| malus           | 13           | malum            | 12              |
|                 |              | male             | 1               |
| ceterus         | 13           | cetera           | 7               |
|                 |              | ceteri           | 6               |
| meus            | 12           | ego              | 10              |
|                 |              | mei              | 2               |
| factum          | 12           | facio            | 12              |
| primus          | 12           | primum           | 12              |
| priusquam       | 11           | quam             | 6               |
|                 |              | qui              | 3               |
|                 |              | antequam         | 1               |
|                 |              | quis             | 1               |
| qua             | 11           | qui              | 6               |
|                 |              | quis             | 5               |
| refero          | 10           | refert           | 10              |
| quantus         | 10           | quantum          | 7               |
|                 |              | quanto           | 3               |
| ardeo           | 9            | ardens           | 9               |
| utor            | 9            | ut               | 7               |
|                 |              | usus             | 2               |
| uerum           | 9            | uerus            | 7               |
|                 |              | uero             | 2               |
| uerus           | 9            | uerum            | 7               |
|                 |              | uero             | 2               |
| magnus          | 9            | maiores          | 8               |
|                 |              | magna            | 1               |
| refert          | 9            | refero           | 9               |
| noster          | 9            | nostri           | 6               |
|                 |              | nos              | 3               |
| falsum          | 9            | falsus           | 9               |
| suum            | 9            | suus             | 9               |
| liber           | 9            | liberi           | 8               |
|                 |              | libero           | 1               |
| soluo           | 8            | solutus          | 8               |
| natus           | 8            | nascor           | 8               |
| futurus         | 8            | sum              | 6               |
|                 |              | futurum          | 2               |
| sacrum          | 8            | sacer            | 8               |
| paro            | 8            | paratus          | 5               |
|                 |              | pareo            | 1               |
|                 |              | par              | 1               |
|                 |              | parate           | 1               |
| nascor          | 7            | natus            | 5               |
|                 |              | nata             | 2               |
| medius          | 7            | medium           | 7               |
| lego            | 7            | lex              | 4               |
|                 |              | lectus           | 3               |
| paratus         | 7            | paro             | 7               |
| apertus         | 7            | aperio           | 5               |
|                 |              | apertum          | 2               |
| ueneo           | 7            | uenio            | 7               |
| altus           | 7            | altum            | 4               |
|                 |              | alte             | 3               |
| exter           | 7            | extremum         | 6               |
|                 |              | extrema          | 1               |
| paucus          | 7            | pauci            | 7               |
| opera           | 7            | opus             | 7               |
| primum          | 7            | primus           | 7               |
| bene            | 7            | bonus            | 7               |
| nostri          | 7            | noster           | 7               |
| consto          | 7            | consisto         | 6               |
|                 |              | constans         | 1               |
| effusus         | 7            | effundo          | 7               |
| mali            | 7            | malus            | 4               |
|                 |              | malum            | 3               |
| reliquus        | 6            | reliqui          | 5               |
|                 |              | reliquum         | 1               |
| totum           | 6            | totus            | 6               |
| nos             | 6            | noster           | 6               |
| aer             | 6            | aes              | 6               |
| unus            | 6            | una              | 5               |
|                 |              | unum             | 1               |
| summa           | 6            | superus          | 6               |
| malum           | 6            | malus            | 4               |
|                 |              | malo             | 1               |
|                 |              | mali             | 1               |
| unum            | 6            | unus             | 6               |
| morior          | 6            | mortuus          | 6               |
| iure            | 6            | ius              | 6               |
| uis             | 6            | uir              | 3               |
|                 |              | uolo             | 3               |
| tuus            | 6            | tui              | 5               |
|                 |              | tuum             | 1               |
| tu              | 6            | tuus             | 6               |
| dubium          | 5            | dubius           | 5               |
| falsus          | 5            | falsum           | 3               |
|                 |              | falso            | 2               |
| sedo            | 5            | sedeo            | 3               |
|                 |              | sedatus          | 2               |
| quantum         | 5            | quantus          | 5               |
| dictum          | 5            | dico             | 5               |
| amo             | 5            | amans            | 4               |
|                 |              | amarus           | 1               |
| meritus         | 5            | mereor           | 2               |
|                 |              | meritum          | 2               |
|                 |              | merito           | 1               |
| uir             | 5            | uis              | 5               |
| multo           | 5            | multus           | 5               |
| ah              | 5            | ab               | 5               |
| sum             | 5            | futurum          | 1               |
|                 |              | ephesus          | 1               |
|                 |              | herus            | 1               |
|                 |              | is               | 1               |
|                 |              | futurus          | 1               |
| propius         | 5            | prope            | 5               |
| probatus        | 5            | probo            | 5               |
| alienum         | 5            | alienus          | 5               |
| una             | 5            | unus             | 5               |
| mereor          | 5            | meritus          | 3               |
|                 |              | merito           | 1               |
|                 |              | meritum          | 1               |
| pascor          | 5            | pasco            | 5               |
| ferus           | 5            | fera             | 3               |
|                 |              | fero             | 2               |
| rego            | 5            | rex              | 5               |
| instructus      | 5            | instruo          | 4               |
|                 |              | instructe        | 1               |
| solitus         | 5            | soleo            | 5               |
| ut              | 5            | utor             | 5               |
| cetera          | 5            | ceterus          | 3               |
|                 |              | ceteri           | 2               |
| compositus      | 5            | compono          | 5               |
| medium          | 5            | medius           | 5               |
| alius           | 5            | alias            | 3               |
|                 |              | alio             | 2               |
| nox             | 5            | nocte            | 5               |
| sacer           | 5            | sacrum           | 5               |
| commodus        | 5            | commodum         | 4               |
|                 |              | commode          | 1               |
| solus           | 5            | sol              | 3               |
|                 |              | solum            | 2               |
| lectus          | 4            | lego             | 4               |
| promissum       | 4            | promitto         | 4               |
| publicus        | 4            | publicum         | 3               |
|                 |              | publicius        | 1               |
| meritum         | 4            | mereor           | 2               |
|                 |              | merito           | 2               |
| cultus          | 4            | colo             | 4               |
| uolo            | 4            | uolens           | 1               |
|                 |              | si               | 1               |
|                 |              | uis              | 1               |
|                 |              | uoluo            | 1               |
| doctus          | 4            | doceo            | 4               |
| mei             | 4            | meus             | 3               |
|                 |              | ego              | 1               |
| armati          | 4            | armatus          | 4               |
| ueteres         | 4            | uetus            | 4               |
| nosco           | 4            | nouus            | 3               |
|                 |              | notus            | 1               |
| superior        | 4            | superus          | 4               |
| dico            | 4            | dictum           | 4               |
| occupatus       | 4            | occupo           | 4               |
| fretus          | 4            | fretum           | 4               |
| ample           | 4            | amplus           | 4               |
| primo           | 4            | primus           | 4               |
| praeteritus     | 4            | praetereo        | 3               |
|                 |              | praeterita       | 1               |
| minimum         | 4            | paruus           | 4               |
| potissimum      | 4            | potius           | 4               |
| exanimus        | 4            | exanimis         | 4               |
| mala            | 4            | malum            | 2               |
|                 |              | malus            | 2               |
| ius             | 4            | iure             | 4               |
| edo             | 4            | editus           | 2               |
|                 |              | sum              | 2               |
| honestum        | 4            | honestus         | 4               |
| modus           | 4            | modo             | 4               |
| comitium        | 4            | comitia          | 4               |
| consulo         | 4            | consul           | 3               |
|                 |              | consultum        | 1               |
| aperio          | 4            | apertus          | 4               |
| crebro          | 4            | creber           | 3               |
|                 |              | crebre           | 1               |
| solum           | 4            | solus            | 4               |
| triginta        | 4            | duo              | 1               |
|                 |              | sex              | 1               |
|                 |              | centum           | 1               |
|                 |              | octo             | 1               |
| reliquum        | 4            | reliquus         | 4               |
| tantum          | 4            | tantus           | 4               |
| acceptus        | 4            | accipio          | 4               |
| caedo           | 4            | cado             | 3               |
|                 |              | caedes           | 1               |
| diuersus        | 4            | diuersum         | 2               |
|                 |              | diuerto          | 2               |
| patior          | 4            | passus           | 2               |
|                 |              | patiens          | 1               |
|                 |              | pando            | 1               |
| pauci           | 4            | paucus           | 4               |
| desertus        | 4            | desero           | 4               |
| nocte           | 4            | nox              | 4               |
| promitto        | 4            | promissum        | 3               |
|                 |              | promissus        | 1               |
| uniuersus       | 4            | uniuersi         | 3               |
|                 |              | uniuersum        | 1               |
| uectigalis      | 4            | uectigal         | 4               |
| os              | 4            | ora              | 4               |
| pareo           | 4            | paro             | 2               |
|                 |              | parens           | 2               |
| uoluo           | 4            | uolo             | 3               |
|                 |              | uoluto           | 1               |
| furo            | 4            | furens           | 4               |
| nota            | 4            | notus            | 4               |
| maiores         | 4            | magnus           | 4               |
| armo            | 4            | armatus          | 3               |
|                 |              | armati           | 1               |
| praecipio       | 4            | praeceptum       | 2               |
|                 |              | praeceps         | 2               |
| dedo            | 4            | do               | 2               |
|                 |              | deditus          | 1               |
|                 |              | deditor          | 1               |
| praesentia      | 3            | praesens         | 3               |
| glycon          | 3            | glycus           | 3               |
| hac             | 3            | hic              | 3               |
| uniuersum       | 3            | uniuersus        | 2               |
|                 |              | uniuersi         | 1               |
| humanus         | 3            | humana           | 2               |
|                 |              | humani           | 1               |
| emineo          | 3            | eminens          | 3               |
| complexus       | 3            | complector       | 3               |
| perdo           | 3            | perditus         | 3               |
| scriptum        | 3            | scribo           | 2               |
|                 |              | scripta          | 1               |
| recipio         | 3            | recepso          | 1               |
|                 |              | receptum         | 1               |
|                 |              | receptus         | 1               |
| supremum        | 3            | superus          | 3               |
| propinquus      | 3            | propinqui        | 3               |
| uideo           | 3            | uisus            | 2               |
|                 |              | uiso             | 1               |
| munitus         | 3            | munio            | 3               |
| modo            | 3            | modus            | 3               |
| spumo           | 3            | spumans          | 3               |
| phoebus         | 3            | phoebe           | 3               |
| serus           | 3            | sero             | 1               |
|                 |              | serum            | 1               |
|                 |              | sera             | 1               |
| mirum           | 3            | mirus            | 3               |
| fera            | 3            | fero             | 3               |
| propono         | 3            | propositum       | 3               |
| uergilius       | 3            | uirgilius        | 3               |
| respondeo       | 3            | responsum        | 3               |
| sisto           | 3            | sto              | 3               |
| pedes           | 3            | pes              | 3               |
| liberi          | 3            | liber            | 3               |
| suspensus       | 3            | suspendo         | 3               |
| soleo           | 3            | solitus          | 2               |
|                 |              | solea            | 1               |
| multa           | 3            | multus           | 3               |
| hospitium       | 3            | hospes           | 3               |
| resido          | 3            | resideo          | 2               |
|                 |              | resis            | 1               |
| proximum        | 3            | propior          | 3               |
| coniungo        | 3            | coniunctus       | 3               |
| numero          | 3            | numerus          | 2               |
|                 |              | numeratus        | 1               |
| secretus        | 3            | secretum         | 3               |
| hadrumetum      | 3            | hadrumentum      | 3               |
| propositum      | 3            | propono          | 3               |
| chiragra        | 3            | cheragra         | 3               |
| externum        | 3            | externi          | 2               |
|                 |              | externus         | 1               |
| tertius         | 3            | decimus          | 2               |
|                 |              | tres             | 1               |
| fictus          | 3            | fictum           | 2               |
|                 |              | fingo            | 1               |
| feruens         | 3            | ferueo           | 3               |
| raptum          | 3            | rapio            | 3               |
| uiginti         | 3            | triginta         | 1               |
|                 |              | quinque          | 1               |
|                 |              | trecenti         | 1               |
| uelum           | 3            | uolo             | 3               |
| exerceo         | 3            | exercitus        | 3               |
| reduco          | 3            | redux            | 2               |
|                 |              | redduco          | 1               |
| altum           | 3            | altus            | 3               |
| tego            | 3            | tectum           | 3               |
| frequens        | 3            | frequentia       | 2               |
|                 |              | frequenter       | 1               |
| illo            | 3            | ille             | 3               |
| tela            | 3            | telum            | 3               |
| mina            | 3            | minae            | 3               |
| illa            | 3            | ille             | 3               |
| defessus        | 3            | defetiscor       | 3               |
| defunctus       | 3            | defungor         | 3               |
| inflatus        | 3            | inflo            | 3               |
| fractus         | 3            | frango           | 3               |
| opus            | 3            | opera            | 3               |
| securis         | 3            | securus          | 3               |
| certus          | 3            | certum           | 3               |
| herus           | 3            | sum              | 3               |
| oblino          | 3            | obliuiscor       | 3               |
| lenis           | 3            | leniter          | 2               |
|                 |              | lene             | 1               |
| ultimus         | 3            | ultimum          | 3               |
| agite           | 3            | ago              | 3               |
| contrarium      | 3            | contrarius       | 3               |
| inceptum        | 3            | incipio          | 3               |
| pendo           | 3            | pendeo           | 3               |
| uolucris        | 3            | uolucer          | 3               |
| quadraginta     | 3            | triginta         | 1               |
|                 |              | quinque          | 1               |
|                 |              | octoginta        | 1               |
| finitimus       | 3            | finitimi         | 3               |
| latus           | 3            | lateo            | 3               |
| tui             | 3            | tuus             | 2               |
|                 |              | tu               | 1               |
| si              | 3            | audeo            | 1               |
|                 |              | sum              | 1               |
|                 |              | sui              | 1               |
| fero            | 3            | latus            | 2               |
|                 |              | ferrum           | 1               |
| uetus           | 3            | ueteres          | 2               |
|                 |              | uetera           | 1               |
| instruo         | 3            | instructus       | 3               |
| bellus          | 3            | bellum           | 3               |
| superuacuum     | 3            | superuacuus      | 3               |
| cos             | 3            | cotes            | 2               |
|                 |              | cautes           | 1               |
| oriens          | 3            | orior            | 3               |
| secretum        | 3            | secretus         | 3               |
| consultum       | 3            | consulo          | 1               |
|                 |              | consulto         | 1               |
|                 |              | senatus          | 1               |
| certum          | 3            | certus           | 3               |
| fors            | 3            | forte            | 3               |
| romanus         | 3            | romani           | 3               |
| audio           | 3            | auditus          | 3               |
| remissus        | 3            | remitto          | 3               |
| minister        | 3            | ministra         | 3               |
| confusus        | 3            | confundo         | 3               |
| communis        | 3            | commune          | 3               |
| intentus        | 3            | intendo          | 3               |
| facilis         | 3            | facile           | 3               |
| uiuo            | 3            | uiuus            | 2               |
|                 |              | uinco            | 1               |
| aro             | 3            | ares             | 2               |
|                 |              | areo             | 1               |
| alienus         | 3            | alienum          | 3               |
| scripta         | 3            | scriptum         | 3               |
| caelestia       | 3            | caelestis        | 2               |
|                 |              | caelestes        | 1               |
| malo            | 3            | malum            | 3               |
| fidens          | 3            | fido             | 3               |
| perditus        | 3            | perdo            | 3               |
| adultera        | 3            | adulter          | 3               |
| propinqui       | 3            | propinquus       | 3               |
| canus           | 3            | canis            | 2               |
|                 |              | cano             | 1               |
| durus           | 3            | durum            | 2               |
|                 |              | dure             | 1               |
| patens          | 3            | pateo            | 3               |
| regius          | 3            | regia            | 3               |
| ratus           | 3            | reor             | 3               |
| plerique        | 2            | plerusque        | 2               |
| consummatus     | 2            | consummo         | 2               |
| lacon           | 2            | laco             | 2               |
| properans       | 2            | propero          | 2               |
| optatus         | 2            | opto             | 2               |
| ora             | 2            | os               | 2               |
| arcanum         | 2            | arcanus          | 2               |
| alio            | 2            | alius            | 2               |
| insitus         | 2            | insero           | 2               |
| opulens         | 2            | opulentus        | 2               |
| paean           | 2            | paeanus          | 2               |
| penna           | 2            | pinna            | 2               |
| secundus        | 2            | secundum         | 2               |
| chersonesus     | 2            | cherronesus      | 1               |
|                 |              | chersonensis     | 1               |
| perses          | 2            | persae           | 1               |
|                 |              | persius          | 1               |
| exercito        | 2            | exercitatus      | 2               |
| aduerto         | 2            | aduersus         | 2               |
| armatus         | 2            | armati           | 2               |
| impensus        | 2            | impendo          | 1               |
|                 |              | impensa          | 1               |
| uincio          | 2            | uinco            | 2               |
| diua            | 2            | diuus            | 2               |
| patrius         | 2            | patria           | 2               |
| parentes        | 2            | parens           | 2               |
| rapio           | 2            | raptum           | 1               |
|                 |              | raptus           | 1               |
| aes             | 2            | aer              | 2               |
| solutus         | 2            | soluo            | 2               |
| nequeo          | 2            | ne               | 1               |
|                 |              | noquus           | 1               |
| extollo         | 2            | effero           | 2               |
| sequens         | 2            | sequor           | 2               |
| imum            | 2            | inferus          | 2               |
| diuersum        | 2            | diuersus         | 2               |
| orno            | 2            | ornatus          | 2               |
| arcanus         | 2            | arcanum          | 2               |
| festus          | 2            | festum           | 2               |
| sparsus         | 2            | spargo           | 2               |
| palleo          | 2            | pallens          | 2               |
| nimius          | 2            | nimium           | 2               |
| gener           | 2            | genus            | 2               |
| conspectus      | 2            | conspicio        | 2               |
| piaculo         | 2            | piaculum         | 2               |
| traduco         | 2            | transduco        | 2               |
| liceo           | 2            | licens           | 1               |
|                 |              | licet            | 1               |
| tres            | 2            | tribus           | 1               |
|                 |              | triginta         | 1               |
| ceteri          | 2            | ceterus          | 2               |
| decretum        | 2            | decerno          | 2               |
| praetorium      | 2            | praetorius       | 2               |
| nuntium         | 2            | nuntius          | 2               |
| uoueo           | 2            | uotum            | 1               |
|                 |              | uotus            | 1               |
| iudico          | 2            | iudex            | 2               |
| accipio         | 2            | acceptus         | 1               |
|                 |              | acceptum         | 1               |
| insidiae        | 2            | hinsidiae        | 2               |
| editus          | 2            | edo              | 2               |
| scio            | 2            | sciens           | 2               |
| sabinus         | 2            | sabini           | 2               |
| circus          | 2            | circum           | 2               |
| dexter          | 2            | dextera          | 2               |
| inuentum        | 2            | inuenio          | 2               |
| socia           | 2            | socius           | 2               |
| partio          | 2            | partia           | 1               |
|                 |              | partior          | 1               |
| arcas           | 2            | arcades          | 2               |
| idem            | 2            | eodem            | 2               |
| cito            | 2            | citatus          | 2               |
| spernendus      | 2            | sperno           | 2               |
| tuto            | 2            | tute             | 1               |
|                 |              | tutus            | 1               |
| consuetus       | 2            | consuesco        | 2               |
| uero            | 2            | uerum            | 1               |
|                 |              | uerus            | 1               |
| assido          | 2            | assideo          | 2               |
| senex           | 2            | senior           | 2               |
| opportunitas    | 2            | oportunitas      | 1               |
|                 |              | opportuitas      | 1               |
| mamercus        | 2            | mamius           | 1               |
|                 |              | mamercum         | 1               |
| desero          | 2            | desertus         | 2               |
| uicinum         | 2            | uicinus          | 2               |
| uester          | 2            | uos              | 1               |
|                 |              | uoster           | 1               |
| nubo            | 2            | nupta            | 2               |
| trecenus        | 2            | tricenus         | 2               |
| centum          | 2            | triginta         | 1               |
|                 |              | octo             | 1               |
| demissus        | 2            | demitto          | 2               |
| phoenices       | 2            | phoenice         | 2               |
| priores         | 2            | prior            | 2               |
| anteeo          | 2            | antideo          | 2               |
| fido            | 2            | fidens           | 2               |
| distinctus      | 2            | distinguo        | 2               |
| exiguus         | 2            | exiguum          | 2               |
| insisto         | 2            | insto            | 2               |
| cano            | 2            | canis            | 2               |
| inferus         | 2            | imum             | 1               |
|                 |              | inferi           | 1               |
| insto           | 2            | instans          | 2               |
| fertum          | 2            | fertus           | 1               |
|                 |              | fero             | 1               |
| sponte          | 2            | spons            | 2               |
| improbus        | 2            | improbo          | 2               |
| immensus        | 2            | immensum         | 2               |
| occido          | 2            | occidens         | 2               |
| artus           | 2            | artum            | 1               |
|                 |              | ars              | 1               |
| diuisor         | 2            | diuido           | 2               |
| pugna           | 2            | pugno            | 2               |
| demitto         | 2            | demissus         | 2               |
| uiuens          | 2            | uiuo             | 2               |
| ago             | 2            | age              | 1               |
|                 |              | actum            | 1               |
| calcar          | 2            | calco            | 2               |
| certo           | 2            | certus           | 2               |
| ille            | 2            | illi             | 1               |
|                 |              | illo             | 1               |
| indi            | 2            | indus            | 2               |
| hic             | 2            | hac              | 1               |
|                 |              | huc              | 1               |
| marius          | 2            | marii            | 2               |
| breuis          | 2            | breui            | 2               |
| rudo            | 2            | rudens           | 1               |
|                 |              | rudus            | 1               |
| mereo           | 2            | meritus          | 1               |
|                 |              | mereor           | 1               |
| seruio          | 2            | seruiens         | 2               |
| serius          | 2            | serium           | 2               |
| pilus           | 2            | pilum            | 2               |
| ne              | 2            | tu               | 1               |
|                 |              | hic              | 1               |
| pilum           | 2            | pilus            | 2               |
| secundum        | 2            | secundus         | 2               |
| feneror         | 2            | feneratus        | 1               |
|                 |              | fenero           | 1               |
| ballista        | 2            | balista          | 2               |
| impeditus       | 2            | impedio          | 2               |
| plerusque       | 2            | plerumque        | 1               |
|                 |              | plerique         | 1               |
| mamilius        | 2            | mamilia          | 2               |
| planum          | 2            | planus           | 2               |
| retendo         | 2            | retineo          | 2               |
| solidum         | 2            | soldus           | 1               |
|                 |              | soldum           | 1               |
| priuo           | 2            | priauo           | 1               |
|                 |              | priuatus         | 1               |
| aduersus        | 2            | aduersum         | 2               |
| praesaepes      | 2            | praesaepe        | 2               |
| obsidio         | 2            | obsidium         | 2               |
| casus           | 2            | casu             | 2               |
| exterreo        | 2            | exterritus       | 2               |
| fundo           | 2            | fusus            | 2               |
| praeteritum     | 2            | praetereo        | 2               |
| suebi           | 2            | sueui            | 2               |
| teia            | 2            | teius            | 2               |
| clathri         | 2            | clater           | 2               |
| falernus        | 2            | falernum         | 2               |
| asperum         | 2            | asper            | 2               |
| aduocatus       | 2            | aduoco           | 2               |
| uerso           | 2            | uersor           | 2               |
| perfectus       | 2            | perficio         | 2               |
| attono          | 2            | attonitus        | 2               |
| didius          | 2            | didia            | 2               |
| album           | 2            | albus            | 2               |
| finitimi        | 2            | finitimus        | 2               |
| aetolus         | 2            | aetola           | 2               |
| uigilans        | 2            | uigilo           | 2               |
| regero          | 2            | rego             | 2               |
| decorus         | 2            | decorum          | 1               |
|                 |              | decus            | 1               |
| fusus           | 2            | fundo            | 2               |
| obsequor        | 2            | obsequens        | 2               |
| danais          | 2            | danai            | 1               |
|                 |              | danaides         | 1               |
| corax           | 2            | coracus          | 1               |
|                 |              | coraca           | 1               |
| albinus         | 2            | albinum          | 2               |
| sol             | 2            | solus            | 1               |
|                 |              | solum            | 1               |
| europe          | 2            | europa           | 2               |
| arte            | 2            | ars              | 2               |
| occidens        | 2            | occido           | 2               |
| seruus          | 2            | seruo            | 2               |
| longus          | 2            | longe            | 2               |
| subnitor        | 2            | subnixus         | 2               |
| inclino         | 2            | inclinatus       | 2               |
| futurum         | 2            | sum              | 1               |
|                 |              | futurus          | 1               |
| procer          | 2            | proceres         | 2               |
| iberus          | 2            | iberi            | 2               |
| florens         | 2            | floreo           | 2               |
| tuum            | 2            | tuus             | 2               |
| assuesco        | 2            | assuetus         | 2               |
| substo          | 2            | subsisto         | 2               |
| instituo        | 2            | institutum       | 2               |
| nata            | 2            | nascor           | 1               |
|                 |              | natus            | 1               |
| duco            | 2            | ductus           | 1               |
|                 |              | ducenti          | 1               |
| illi            | 2            | ille             | 2               |
| cumulatus       | 2            | cumulate         | 1               |
|                 |              | cumulo           | 1               |
| pleraque        | 2            | plerusque        | 2               |
| pacatus         | 2            | paco             | 1               |
|                 |              | pacate           | 1               |
| parum           | 2            | paruus           | 2               |
| occultum        | 2            | occultus         | 2               |
| quisque         | 2            | quoque           | 2               |
| magnum          | 2            | magnus           | 2               |
| natis           | 2            | natus            | 1               |
|                 |              | nates            | 1               |
| orbus           | 2            | orbis            | 2               |
| occultus        | 2            | occultum         | 2               |
| huc             | 2            | hic              | 2               |
| latinus         | 2            | latini           | 2               |
| colo            | 2            | cultus           | 2               |
| ego             | 2            | meus             | 2               |
| illim           | 2            | illinc           | 2               |
| fallo           | 2            | falsus           | 2               |
| colchi          | 2            | colchis          | 2               |
| inane           | 2            | inanis           | 2               |
| macedo          | 2            | macedones        | 2               |
| graecus         | 2            | graeci           | 2               |
| desino          | 2            | desum            | 2               |
| uenturum        | 2            | uenio            | 2               |
| aduersum        | 2            | aduersus         | 2               |
| captiua         | 2            | captiuus         | 2               |
| subito          | 2            | subitus          | 2               |
| concupio        | 2            | concupisco       | 2               |
| summum          | 2            | summa            | 2               |
| dubius          | 2            | dubium           | 2               |
| mortuus         | 2            | morior           | 2               |
| scriptor        | 2            | scripta          | 2               |
| abdo            | 2            | abditus          | 2               |
| exterritus      | 2            | exterreo         | 2               |
| caueo           | 2            | cautus           | 1               |
|                 |              | cauea            | 1               |
| mixtus          | 2            | misceo           | 2               |
| compactus       | 2            | compingo         | 2               |
| absens          | 2            | absum            | 2               |
| furens          | 2            | furo             | 2               |
| coma            | 2            | comis            | 2               |
| inferiores      | 2            | inferus          | 2               |
| uenio           | 2            | uenus            | 1               |
|                 |              | ueneo            | 1               |
| tranquillum     | 2            | tranquillus      | 2               |
| natalis         | 2            | natales          | 2               |
| octo            | 2            | triginta         | 1               |
|                 |              | tres             | 1               |
| uallus          | 2            | uallum           | 1               |
|                 |              | uallis           | 1               |
| muraena         | 2            | murena           | 2               |
| numquis         | 2            | numquid          | 1               |
|                 |              | numqua           | 1               |
| sublimis        | 2            | sublime          | 1               |
|                 |              | sublimiter       | 1               |
| quoque          | 2            | quisque          | 2               |
| pario           | 2            | pareo            | 1               |
|                 |              | pars             | 1               |
| torreo          | 2            | torrens          | 2               |
| eadem           | 2            | idem             | 2               |
| discribo        | 2            | describo         | 2               |
| pingo           | 2            | pictus           | 2               |
| ultimum         | 2            | ultimus          | 2               |
| uiride          | 2            | uiridis          | 2               |
| exploratus      | 2            | exploro          | 2               |
| suesco          | 2            | suetus           | 2               |
| digno           | 2            | dignor           | 2               |
| insigne         | 2            | insignis         | 2               |
| laudo           | 2            | laus             | 2               |
| mandatum        | 2            | mando            | 2               |
| progne          | 2            | procne           | 1               |
|                 |              | procnes          | 1               |
| moratus         | 2            | moror            | 2               |
| iudex           | 2            | iudicium         | 2               |
| potius          | 2            | potis            | 1               |
|                 |              | potissimum       | 1               |
| spectatus       | 2            | specto           | 2               |
| mando           | 2            | mandatus         | 1               |
|                 |              | mandatum         | 1               |
| fretum          | 2            | fretus           | 2               |
| crystallinus    | 2            | crustallinum     | 2               |
| operio          | 2            | opertum          | 1               |
|                 |              | opus             | 1               |
| fabricor        | 2            | fabrico          | 2               |
| egeo            | 2            | ago              | 2               |
| fortuita        | 2            | fortuitus        | 2               |
| uniuersi        | 2            | uniuersus        | 2               |
| ratis           | 2            | reor             | 2               |
| posteaquam      | 2            | quam             | 1               |
|                 |              | priusquam        | 1               |
| milon           | 2            | milo             | 2               |
| geminus         | 2            | gemini           | 2               |
| uisum           | 2            | uisus            | 1               |
|                 |              | uideo            | 1               |
| opto            | 2            | optatus          | 2               |
| meum            | 2            | meus             | 2               |
| concretus       | 2            | concresco        | 2               |
| nucleus         | 2            | nuculeus         | 2               |
| tyriotes        | 2            | tyrio            | 1               |
|                 |              | tyriotus         | 1               |
| myoparon        | 2            | myoparus         | 2               |
| capto           | 2            | capio            | 2               |
| praeterita      | 2            | praetereo        | 1               |
|                 |              | praeteritus      | 1               |
| posterus        | 2            | postumus         | 1               |
|                 |              | posterius        | 1               |
| amplius         | 2            | ample            | 1               |
|                 |              | amplus           | 1               |
| uersus          | 2            | uerto            | 2               |
| porsena         | 2            | porsina          | 2               |
| miliarius       | 1            | millaria         | 1               |
| plaustellum     | 1            | plautellus       | 1               |
| mus             | 1            | murus            | 1               |
| lex             | 1            | lego             | 1               |
| cubitus         | 1            | cubitum          | 1               |
| connecto        | 1            | connexus         | 1               |
| podex           | 1            | paudex           | 1               |
| pelion          | 1            | peleus           | 1               |
| plecto          | 1            | plexus           | 1               |
| amplexus        | 1            | amplector        | 1               |
| abscisus        | 1            | abscido          | 1               |
| oculissimus     | 1            | oculus           | 1               |
| graue           | 1            | grauiter         | 1               |
| erratum         | 1            | erro             | 1               |
| speratum        | 1            | spero            | 1               |
| teucer          | 1            | teucri           | 1               |
| quatuordecim    | 1            | quatuor          | 1               |
| iapydia         | 1            | iapydius         | 1               |
| totus           | 1            | totum            | 1               |
| diuinus         | 1            | diuina           | 1               |
| afficio         | 1            | affectus         | 1               |
| annia           | 1            | annius           | 1               |
| heraclea        | 1            | heraclia         | 1               |
| uirilia         | 1            | uirile           | 1               |
| mora            | 1            | mos              | 1               |
| tanto           | 1            | tantus           | 1               |
| emeritus        | 1            | emereor          | 1               |
| abitus          | 1            | abeo             | 1               |
| dispositura     | 1            | dispono          | 1               |
| clodius         | 1            | clodia           | 1               |
| circumfundo     | 1            | circum           | 1               |
| isti            | 1            | iste             | 1               |
| fastus          | 1            | fastuus          | 1               |
| albucius        | 1            | albucus          | 1               |
| memoro          | 1            | memor            | 1               |
| obtueor         | 1            | obtuo            | 1               |
| rescio          | 1            | rescisco         | 1               |
| ischiacus       | 1            | isciacus         | 1               |
| iuniperus       | 1            | iunipirus        | 1               |
| congius         | 1            | congium          | 1               |
| tralliani       | 1            | trallianus       | 1               |
| maeandrius      | 1            | maeander         | 1               |
| auriferus       | 1            | aurifer          | 1               |
| saeuio          | 1            | saeuus           | 1               |
| distringo       | 1            | districtus       | 1               |
| inaffecto       | 1            | inadfecto        | 1               |
| disicio         | 1            | dissicio         | 1               |
| consanguinea    | 1            | consanguineus    | 1               |
| deperditus      | 1            | deperdo          | 1               |
| parraces        | 1            | parrax           | 1               |
| saepta          | 1            | saeptum          | 1               |
| dyrrachini      | 1            | dyrrachinus      | 1               |
| iecur           | 1            | iocinus          | 1               |
| lampsaceni      | 1            | lampsacenus      | 1               |
| iacto           | 1            | iacio            | 1               |
| pecoli          | 1            | pecolis          | 1               |
| femen           | 1            | femur            | 1               |
| helene          | 1            | helena           | 1               |
| sescenti        | 1            | quadraginta      | 1               |
| sulpicia        | 1            | sulpicius        | 1               |
| nubilum         | 1            | nubila           | 1               |
| compositum      | 1            | compono          | 1               |
| librarius       | 1            | libro            | 1               |
| elementa        | 1            | elementum        | 1               |
| mutitio         | 1            | muttitio         | 1               |
| cunica          | 1            | cunicus          | 1               |
| labia           | 1            | labea            | 1               |
| bifarius        | 1            | bifaria          | 1               |
| memorandus      | 1            | memoro           | 1               |
| stellio         | 1            | stelium          | 1               |
| miscellaneus    | 1            | miscellanea      | 1               |
| sabbatum        | 1            | sabbata          | 1               |
| milium          | 1            | mille            | 1               |
| obsurdesco      | 1            | obsurdo          | 1               |
| manes           | 1            | manus            | 1               |
| intestinum      | 1            | intestinus       | 1               |
| iuratus         | 1            | iuro             | 1               |
| exoptatus       | 1            | exopto           | 1               |
| internuntius    | 1            | internuntium     | 1               |
| perdoctus       | 1            | perdoceo         | 1               |
| pomeiani        | 1            | pompeiani        | 1               |
| puls            | 1            | pultus           | 1               |
| quassus         | 1            | quatio           | 1               |
| comis           | 1            | comes            | 1               |
| misena          | 1            | misenis          | 1               |
| proagorus       | 1            | proagor          | 1               |
| clare           | 1            | clarus           | 1               |
| circulor        | 1            | circulo          | 1               |
| imbrus          | 1            | imber            | 1               |
| creta           | 1            | cresco           | 1               |
| ingemisco       | 1            | ingemo           | 1               |
| lapithae        | 1            | lapithus         | 1               |
| dispergo        | 1            | dispargo         | 1               |
| mytilene        | 1            | mytilena         | 1               |
| tetre           | 1            | teteriter        | 1               |
| ramale          | 1            | ramalium         | 1               |
| diligo          | 1            | dilectus         | 1               |
| falso           | 1            | falsus           | 1               |
| floreo          | 1            | florens          | 1               |
| permixtus       | 1            | permisceo        | 1               |
| insiticius      | 1            | insiticium       | 1               |
| graeculi        | 1            | graeculus        | 1               |
| condio          | 1            | condo            | 1               |
| cellarius       | 1            | cellarium        | 1               |
| opimius         | 1            | opimus           | 1               |
| opertum         | 1            | operio           | 1               |
| terni           | 1            | ternus           | 1               |
| uiaticum        | 1            | uiaticus         | 1               |
| sollemnis       | 1            | sollemne         | 1               |
| congruens       | 1            | congruo          | 1               |
| caecilia        | 1            | caecilius        | 1               |
| nugor           | 1            | nugo             | 1               |
| librator        | 1            | libritor         | 1               |
| acte            | 1            | actes            | 1               |
| honestas        | 1            | honestus         | 1               |
| repono          | 1            | repositus        | 1               |
| sexcenus        | 1            | sescenus         | 1               |
| caius           | 1            | cais             | 1               |
| actum           | 1            | ago              | 1               |
| legulus         | 1            | legula           | 1               |
| supra           | 1            | semis            | 1               |
| uos             | 1            | uester           | 1               |
| circumgemo      | 1            | circumgo         | 1               |
| ebulum          | 1            | ebulus           | 1               |
| rubeo           | 1            | rubens           | 1               |
| agon            | 1            | agona            | 1               |
| terrestris      | 1            | terrestre        | 1               |
| iugosus         | 1            | iugosum          | 1               |
| euocatus        | 1            | euoco            | 1               |
| oscen           | 1            | oscinis          | 1               |
| uigiliarium     | 1            | uigilarium       | 1               |
| sardus          | 1            | sarda            | 1               |
| aequiparo       | 1            | aequipero        | 1               |
| comitatus       | 1            | comitor          | 1               |
| grates          | 1            | gratus           | 1               |
| luca            | 1            | lucae            | 1               |
| montanus        | 1            | montani          | 1               |
| prospera        | 1            | prosper          | 1               |
| bidinus         | 1            | bidini           | 1               |
| syracusanus     | 1            | syracusani       | 1               |
| ecquid          | 1            | ecquis           | 1               |
| senus           | 1            | senex            | 1               |
| honesti         | 1            | honestus         | 1               |
| latius          | 1            | latium           | 1               |
| purgo           | 1            | purgatus         | 1               |
| perpetuum       | 1            | perpetuus        | 1               |
| lateo           | 1            | late             | 1               |
| perturbo        | 1            | perturbatus      | 1               |
| commodum        | 1            | chommoda         | 1               |
| patria          | 1            | patrius          | 1               |
| seminarium      | 1            | seminarius       | 1               |
| lydius          | 1            | lydia            | 1               |
| sectiuus        | 1            | sectio           | 1               |
| porrum          | 1            | porrus           | 1               |
| pactus          | 1            | paciscor         | 1               |
| gero            | 1            | gestus           | 1               |
| lentus          | 1            | lente            | 1               |
| cannabis        | 1            | cannabes         | 1               |
| ueientanus      | 1            | ueiientanus      | 1               |
| affectus        | 1            | afficio          | 1               |
| thrasyllus      | 1            | thrasullus       | 1               |
| albanum         | 1            | albanus          | 1               |
| surrentinum     | 1            | surrentinus      | 1               |
| deliquus        | 1            | delicuus         | 1               |
| phoronis        | 1            | phoronides       | 1               |
| argi            | 1            | argus            | 1               |
| auriga          | 1            | aurigis          | 1               |
| defrico         | 1            | defringo         | 1               |
| arduus          | 1            | arduum           | 1               |
| numquid         | 1            | numquis          | 1               |
| affirmate       | 1            | affirmo          | 1               |
| solito          | 1            | solitum          | 1               |
| suscipio        | 1            | susceptus        | 1               |
| grauo           | 1            | grauor           | 1               |
| emoderor        | 1            | emodero          | 1               |
| pressus         | 1            | premo            | 1               |
| superfluo       | 1            | superfluens      | 1               |
| uenundo         | 1            | uenumdo          | 1               |
| ulterior        | 1            | ulteriora        | 1               |
| tactus          | 1            | tango            | 1               |
| gregarius       | 1            | gregarium        | 1               |
| inductus        | 1            | induco           | 1               |
| ueles           | 1            | ueletes          | 1               |
| ueliensis       | 1            | uelienses        | 1               |
| seuerus         | 1            | sero             | 1               |
| cautes          | 1            | cotes            | 1               |
| pompei          | 1            | pompeius         | 1               |
| fingo           | 1            | fictum           | 1               |
| hippodromos     | 1            | hippodromus      | 1               |
| prouidens       | 1            | prouideo         | 1               |
| comptus         | 1            | como             | 1               |
| mapalia         | 1            | mapalis          | 1               |
| ulteriora       | 1            | ulterior         | 1               |
| materior        | 1            | materio          | 1               |
| gorge           | 1            | gorgus           | 1               |
| incitatus       | 1            | incito           | 1               |
| iarbas          | 1            | iarba            | 1               |
| satisfacio      | 1            | facissesatus     | 1               |
| custos          | 1            | custodio         | 1               |
| coeptum         | 1            | coepio           | 1               |
| munio           | 1            | munitus          | 1               |
| celendris       | 1            | celendes         | 1               |
| ocrea           | 1            | ocreo            | 1               |
| sempiterno      | 1            | sempiternus      | 1               |
| zaplutus        | 1            | saplutus         | 1               |
| cerno           | 1            | cresco           | 1               |
| inicio          | 1            | iniactus         | 1               |
| tumulo          | 1            | tumulor          | 1               |
| em              | 1            | hem              | 1               |
| apollonidenses  | 1            | apollonidensis   | 1               |
| triumpho        | 1            | triumphus        | 1               |
| mulsum          | 1            | mulso            | 1               |
| calidus         | 1            | caldus           | 1               |
| morigerus       | 1            | moriger          | 1               |
| lacerta         | 1            | lacertum         | 1               |
| sera            | 1            | serus            | 1               |
| como            | 1            | comans           | 1               |
| pallens         | 1            | palleo           | 1               |
| aura            | 1            | auris            | 1               |
| perualeo        | 1            | perualo          | 1               |
| impello         | 1            | impulsus         | 1               |
| scelestus       | 1            | sceleste         | 1               |
| libella         | 1            | libellus         | 1               |
| uicenus         | 1            | uicerius         | 1               |
| admiror         | 1            | admirandus       | 1               |
| timens          | 1            | timeo            | 1               |
| ornatus         | 1            | orno             | 1               |
| sesama          | 1            | sesimus          | 1               |
| exserto         | 1            | exerto           | 1               |
| benefactum      | 1            | benefacio        | 1               |
| incestum        | 1            | incestus         | 1               |
| subcerno        | 1            | subcero          | 1               |
| pauio           | 1            | paueo            | 1               |
| improuiso       | 1            | improuisus       | 1               |
| conseruo        | 1            | conseruus        | 1               |
| baucis          | 1            | bauci            | 1               |
| ocimum          | 1            | ocima            | 1               |
| craterus        | 1            | crater           | 1               |
| auctus          | 1            | augeo            | 1               |
| dextrorsum      | 1            | dextrouersus     | 1               |
| improperatus    | 1            | impropero        | 1               |
| macte           | 1            | mactus           | 1               |
| pullo           | 1            | pullus           | 1               |
| gallinaceus     | 1            | gallinacius      | 1               |
| noceo           | 1            | nocitus          | 1               |
| frenum          | 1            | freni            | 1               |
| uox             | 1            | uoco             | 1               |
| gillo           | 1            | gillus           | 1               |
| fungus          | 1            | fungor           | 1               |
| tarpeia         | 1            | tarpeius         | 1               |
| dipondius       | 1            | duponde          | 1               |
| eruditi         | 1            | eruditus         | 1               |
| buxus           | 1            | buxum            | 1               |
| segimundus      | 1            | segimundum       | 1               |
| accensus        | 1            | accensum         | 1               |
| radians         | 1            | radio            | 1               |
| acilius         | 1            | acilia           | 1               |
| cotylo          | 1            | cotylus          | 1               |
| ludicrum        | 1            | ludicer          | 1               |
| dorsum          | 1            | dordeo           | 1               |
| formica         | 1            | formix           | 1               |
| consus          | 1            | consis           | 1               |
| lar             | 1            | larus            | 1               |
| mutuo           | 1            | mutuus           | 1               |
| conspicuum      | 1            | conspicuus       | 1               |
| flagro          | 1            | flagrans         | 1               |
| directus        | 1            | dirigo           | 1               |
| improuisum      | 1            | improuisus       | 1               |
| taxiles         | 1            | taxilus          | 1               |
| attero          | 1            | attritus         | 1               |
| amplus          | 1            | ample            | 1               |
| babylonii       | 1            | babylonius       | 1               |
| exiguum         | 1            | exiguus          | 1               |
| defectus        | 1            | deficio          | 1               |
| clio            | 1            | clius            | 1               |
| ascra           | 1            | ascrus           | 1               |
| ductus          | 1            | duco             | 1               |
| haustus         | 1            | haurio           | 1               |
| actus           | 1            | ago              | 1               |
| serpo           | 1            | serpus           | 1               |
| phidyle         | 1            | phidylus         | 1               |
| placo           | 1            | placeo           | 1               |
| geryon          | 1            | geryone          | 1               |
| cinipes         | 1            | sciniphes        | 1               |
| cometes         | 1            | comes            | 1               |
| uectigal        | 1            | uectigalis       | 1               |
| coleus          | 1            | coleum           | 1               |
| luscus          | 1            | lusce            | 1               |
| arretium        | 1            | arretius         | 1               |
| indulgeo        | 1            | indulgens        | 1               |
| fundanus        | 1            | fundanius        | 1               |
| comparo         | 1            | compara          | 1               |
| durum           | 1            | durus            | 1               |
| lycia           | 1            | lycius           | 1               |
| utilis          | 1            | utile            | 1               |
| demens          | 1            | dementia         | 1               |
| lino            | 1            | linum            | 1               |
| arrogans        | 1            | arroganter       | 1               |
| hernici         | 1            | hernicus         | 1               |
| obsto           | 1            | obsisto          | 1               |
| cursura         | 1            | curro            | 1               |
| depositum       | 1            | depono           | 1               |
| subrufus        | 1            | subrufo          | 1               |
| cincinnatus     | 1            | cincinno         | 1               |
| merx            | 1            | mercium          | 1               |
| exsugeo         | 1            | exsugo           | 1               |
| committo        | 1            | commissum        | 1               |
| aliorsum        | 1            | aliouersus       | 1               |
| illuc           | 1            | illic            | 1               |
| gallograeci     | 1            | gallograecus     | 1               |
| pronubus        | 1            | pronuba          | 1               |
| librariolus     | 1            | librarionus      | 1               |
| piratica        | 1            | piraticus        | 1               |
| notus           | 1            | nota             | 1               |
| consilium       | 1            | consilis         | 1               |
| impingo         | 1            | impictus         | 1               |
| expressus       | 1            | exprimo          | 1               |
| stratum         | 1            | sterno           | 1               |
| lepos           | 1            | lepor            | 1               |
| capitulum       | 1            | capitulus        | 1               |
| deformo         | 1            | deformatus       | 1               |
| suionae         | 1            | suiones          | 1               |
| cludo           | 1            | claudo           | 1               |
| iubeo           | 1            | iussum           | 1               |
| romuleus        | 1            | romilia          | 1               |
| scyrius         | 1            | scyria           | 1               |
| candeo          | 1            | candens          | 1               |
| amicio          | 1            | amictus          | 1               |
| uer             | 1            | uerus            | 1               |
| inertia         | 1            | iners            | 1               |
| obtrudo         | 1            | obstrudo         | 1               |
| tinea           | 1            | tinia            | 1               |
| studiosus       | 1            | studiose         | 1               |
| compono         | 1            | compositus       | 1               |
| honoro          | 1            | honoratus        | 1               |
| memor           | 1            | memoro           | 1               |
| philetas        | 1            | philitas         | 1               |
| eburnus         | 1            | eburneus         | 1               |
| phoenicopterus  | 1            | phoenicopter     | 1               |
| corinthia       | 1            | corinthium       | 1               |
| initiamenta     | 1            | initiamentum     | 1               |
| thalestris      | 1            | thalestra        | 1               |
| honestus        | 1            | honestum         | 1               |
| praescribo      | 1            | praescriptum     | 1               |
| resideo         | 1            | resido           | 1               |
| choraules       | 1            | choraula         | 1               |
| inanis          | 1            | inane            | 1               |
| praecompono     | 1            | praecompositus   | 1               |
| curtius         | 1            | curtii           | 1               |
| memmius         | 1            | memmii           | 1               |
| epicurei        | 1            | epicureus        | 1               |
| suauium         | 1            | suaua            | 1               |
| tiro            | 1            | tirus            | 1               |
| bulbus          | 1            | bulba            | 1               |
| threissa        | 1            | threissus        | 1               |
| praeuertor      | 1            | praeuerto        | 1               |
| nitrum          | 1            | nitro            | 1               |
| tango           | 1            | tactus           | 1               |
| ecquis          | 1            | ecquid           | 1               |
| inflo           | 1            | infla            | 1               |
| inclamito       | 1            | inclamitor       | 1               |
| tamesis         | 1            | tamesa           | 1               |
| mufrius         | 1            | mufer            | 1               |
| misere          | 1            | mitto            | 1               |
| pecuarius       | 1            | pecuarium        | 1               |
| exercitium      | 1            | exercitio        | 1               |
| noxia           | 1            | noxius           | 1               |
| par             | 1            | paro             | 1               |
| coele           | 1            | coeles           | 1               |
| cupiens         | 1            | cupio            | 1               |
| procliuis       | 1            | procliue         | 1               |
| impedio         | 1            | impeditus        | 1               |
| liqueo          | 1            | liquor           | 1               |
| oneraria        | 1            | onerarius        | 1               |
| antonia         | 1            | antonius         | 1               |
| romani          | 1            | romanus          | 1               |
| aliquantus      | 1            | aliquanto        | 1               |
| pes             | 1            | pedes            | 1               |
| mysus           | 1            | myse             | 1               |
| alternis        | 1            | alternus         | 1               |
| absolutus       | 1            | absoluo          | 1               |
| effutuo         | 1            | effututus        | 1               |
| agamemnonides   | 1            | agamemnonidae    | 1               |
| subripio        | 1            | surripio         | 1               |
| possido         | 1            | possideo         | 1               |
| sanctus         | 1            | sancti           | 1               |
| fandus          | 1            | for              | 1               |
| eratosthenes    | 1            | eratosthenus     | 1               |
| graeci          | 1            | graecus          | 1               |
| orcynia         | 1            | orcynius         | 1               |
| uolcae          | 1            | uulca            | 1               |
| rhode           | 1            | rhodus           | 1               |
| thimiamae       | 1            | thimiama         | 1               |
| regens          | 1            | rego             | 1               |
| diuinum         | 1            | diuinus          | 1               |
| afflictus       | 1            | affligo          | 1               |
| depressus       | 1            | deprimo          | 1               |
| exilis          | 1            | exsilium         | 1               |
| plaudo          | 1            | plodo            | 1               |
| syngrapha       | 1            | syngraphus       | 1               |
| audiens         | 1            | audio            | 1               |
| uisus           | 1            | uideo            | 1               |
| operor          | 1            | operatus         | 1               |
| uicesimanus     | 1            | uicesimani       | 1               |
| bifer           | 1            | biferus          | 1               |
| diffusus        | 1            | diffundo         | 1               |
| reor            | 1            | ratis            | 1               |
| familiaris      | 1            | familiariter     | 1               |
| porrigo         | 1            | porgo            | 1               |
| abditum         | 1            | abdo             | 1               |
| deprauo         | 1            | depraueo         | 1               |
| monstruosus     | 1            | monstrosus       | 1               |
| distortus       | 1            | distorqueo       | 1               |
| ocius           | 1            | ociter           | 1               |
| pergamus        | 1            | pergamum         | 1               |
| appeto          | 1            | appetens         | 1               |
| duellum         | 1            | duella           | 1               |
| britto          | 1            | britton          | 1               |
| sauromatae      | 1            | sauromata        | 1               |
| fictilis        | 1            | fictile          | 1               |
| lux             | 1            | lucus            | 1               |
| superuacuus     | 1            | superuacuum      | 1               |
| cibyrata        | 1            | cibyratae        | 1               |
| uermina         | 1            | uermen           | 1               |
| angularis       | 1            | angulo           | 1               |
| fulmenta        | 1            | fulmentus        | 1               |
| legatum         | 1            | legatus          | 1               |
| stillicidium    | 1            | stillicidia      | 1               |
| subleuo         | 1            | subleuis         | 1               |
| pateo           | 1            | patior           | 1               |
| arrogo          | 1            | arrogans         | 1               |
| lanigera        | 1            | laniger          | 1               |
| incesso         | 1            | incedo           | 1               |
| commodo         | 1            | commodus         | 1               |
| abrogo          | 1            | arrogo           | 1               |
| cautus          | 1            | caueo            | 1               |
| gusto           | 1            | gustatus         | 1               |
| syri            | 1            | syrus            | 1               |
| frux            | 1            | frugi            | 1               |
| lepus           | 1            | lepor            | 1               |
| pio             | 1            | pies             | 1               |
| uanum           | 1            | uanus            | 1               |
| aeneum          | 1            | aeneus           | 1               |
| tondeo          | 1            | tonde            | 1               |
| ineptia         | 1            | ineptiae         | 1               |
| incipisso       | 1            | incipio          | 1               |
| lautus          | 1            | lauo             | 1               |
| cretatus        | 1            | creto            | 1               |
| ambitio         | 1            | ambitius         | 1               |
| cerialia        | 1            | cerealis         | 1               |
| liquidum        | 1            | liquidus         | 1               |
| properus        | 1            | propero          | 1               |
| conuentus       | 1            | conuenio         | 1               |
| chius           | 1            | chias            | 1               |
| margaritum      | 1            | margaritus       | 1               |
| audeo           | 1            | audens           | 1               |
| siculus         | 1            | siculi           | 1               |
| aracinthus      | 1            | aracynthus       | 1               |
| utile           | 1            | utilis           | 1               |
| asellus         | 1            | asellis          | 1               |
| anticyra        | 1            | anticyrus        | 1               |
| quinquagenus    | 1            | quinquageni      | 1               |
| capsa           | 1            | capso            | 1               |
| sophisma        | 1            | sophismatum      | 1               |
| poeas           | 1            | poeans           | 1               |
| ituraei         | 1            | ituraeus         | 1               |
| laus            | 1            | laudo            | 1               |
| emendatus       | 1            | emendo           | 1               |
| caecilius       | 1            | caecilia         | 1               |
| exardeo         | 1            | exardesco        | 1               |
| carteinensis    | 1            | carteienses      | 1               |
| blandus         | 1            | blandior         | 1               |
| recuruo         | 1            | recuruus         | 1               |
| palumbus        | 1            | palumbum         | 1               |
| morigero        | 1            | morigerus        | 1               |
| antistita       | 1            | antistitas       | 1               |
| aurichalcum     | 1            | aurichalcus      | 1               |
| meto            | 1            | meta             | 1               |
| acer            | 1            | acriter          | 1               |
| uiuus           | 1            | uiuo             | 1               |
| status          | 1            | statuo           | 1               |
| ferrum          | 1            | fero             | 1               |
| borysthenidae   | 1            | borysthenides    | 1               |
| anaticula       | 1            | aneticula        | 1               |
| torquis         | 1            | torquio          | 1               |
| imperiosus      | 1            | imperiose        | 1               |
| senectus        | 1            | senecta          | 1               |
| insalutatus     | 1            | saluto           | 1               |
| absconditus     | 1            | abscondo         | 1               |
| receptus        | 1            | recipio          | 1               |
| tarracinensis   | 1            | terracinensis    | 1               |
| palimpsestus    | 1            | palimpsestos     | 1               |
| simile          | 1            | simillime        | 1               |
| hibernia        | 1            | iuuerna          | 1               |
| uetitum         | 1            | ueto             | 1               |
| cirrati         | 1            | cirrator         | 1               |
| sequor          | 1            | sequens          | 1               |
| interdico       | 1            | interdictum      | 1               |
| macelo          | 1            | macelus          | 1               |
| petulanter      | 1            | petulans         | 1               |
| dispando        | 1            | dispessus        | 1               |
| recte           | 1            | rectus           | 1               |
| pondo           | 1            | pes              | 1               |
| hederaceus      | 1            | hederacia        | 1               |
| submitto        | 1            | submissus        | 1               |
| oenotrius       | 1            | oenotria         | 1               |
| incubo          | 1            | incumbo          | 1               |
| decimus         | 1            | decem            | 1               |
| compactum       | 1            | compectus        | 1               |
| irritatus       | 1            | irrito           | 1               |
| exsugo          | 1            | exuctus          | 1               |
| motus           | 1            | moueo            | 1               |
| cella           | 1            | cello            | 1               |
| assentio        | 1            | assentior        | 1               |
| locusta         | 1            | locustus         | 1               |
| hiccine         | 1            | hic              | 1               |
| inquinatus      | 1            | inquino          | 1               |
| insideo         | 1            | insido           | 1               |
| accido          | 1            | accidens         | 1               |
| maximus         | 1            | magnus           | 1               |
| care            | 1            | carus            | 1               |
| amiculus        | 1            | amiculum         | 1               |
| perdomo         | 1            | perdomitor       | 1               |
| cani            | 1            | canus            | 1               |
| gnosia          | 1            | gnosius          | 1               |
| andromeda       | 1            | andromede        | 1               |
| edonis          | 1            | edoni            | 1               |
| canninefas      | 1            | canninefates     | 1               |
| alias           | 1            | alius            | 1               |
| difficile       | 1            | difficilis       | 1               |
| dure            | 1            | durus            | 1               |
| amans           | 1            | amo              | 1               |
| erigo           | 1            | erectus          | 1               |
| laserpicium     | 1            | laserpitium      | 1               |
| sollemne        | 1            | sollemnis        | 1               |
| nauigo          | 1            | nauigans         | 1               |
| detectus        | 1            | detego           | 1               |
| aestuo          | 1            | aestuus          | 1               |
| uiuiradix       | 1            | uiueradix        | 1               |
| suburbani       | 1            | suburbanus       | 1               |
| obsido          | 1            | obsideo          | 1               |
| fraces          | 1            | fraco            | 1               |
| uolucer         | 1            | uolucris         | 1               |
| percontor       | 1            | percunctor       | 1               |
| asicius         | 1            | asicus           | 1               |
| laniatus        | 1            | lanio            | 1               |
| barbare         | 1            | barbarus         | 1               |
| praesto         | 1            | praestans        | 1               |
| uelox           | 1            | uelociter        | 1               |
| salentini       | 1            | sallentinus      | 1               |
| philocteta      | 1            | philoctetes      | 1               |
| petelia         | 1            | petelius         | 1               |
| propnigeum      | 1            | propnigeo        | 1               |
| qualibet        | 1            | quilibet         | 1               |
| iunior          | 1            | iuuenis          | 1               |
| aequo           | 1            | aequus           | 1               |
| uerumuero       | 1            | uerumo           | 1               |
| quadra          | 1            | quadrum          | 1               |
| inuius          | 1            | inuia            | 1               |
| ordouices       | 1            | ordouicus        | 1               |
| cytaeis         | 1            | cytaeus          | 1               |
| perimedeus      | 1            | perimedaeus      | 1               |
| acquiesco       | 1            | acquio           | 1               |
| uirgilius       | 1            | uergilius        | 1               |
| fortiter        | 1            | fortis           | 1               |
| trasimenus      | 1            | trasimena        | 1               |
| aestiuus        | 1            | aestiua          | 1               |
| prima           | 1            | primus           | 1               |
| amicus          | 1            | amicius          | 1               |
| iatraliptes     | 1            | iatralipta       | 1               |
| expensum        | 1            | expendo          | 1               |
| paluster        | 1            | palustris        | 1               |
| supersum        | 1            | sum              | 1               |
| eodem           | 1            | idem             | 1               |
| aspicio         | 1            | aspectus         | 1               |
| obedio          | 1            | obediens         | 1               |
| singulus        | 1            | singula          | 1               |
| parthi          | 1            | parthus          | 1               |
| nex             | 1            | neco             | 1               |
| ferrea          | 1            | ferreus          | 1               |
| sarculum        | 1            | sarcula          | 1               |
| incile          | 1            | incilis          | 1               |
| occo            | 1            | occa             | 1               |
| dolens          | 1            | doleo            | 1               |
| catillum        | 1            | catilla          | 1               |
| statunculum     | 1            | statuncula       | 1               |
| uerno           | 1            | uernus           | 1               |
| futuri          | 1            | futurum          | 1               |
| dianius         | 1            | dianium          | 1               |
| donum           | 1            | dono             | 1               |
| intumulatus     | 1            | intumulor        | 1               |
| perforo         | 1            | foro             | 1               |
| auditum         | 1            | audio            | 1               |
| sollicito       | 1            | sollicitus       | 1               |
| pan             | 1            | pani             | 1               |
| sobrina         | 1            | sobrinus         | 1               |
| irridiculum     | 1            | irridiculus      | 1               |
| anguste         | 1            | angustus         | 1               |
| peruagatus      | 1            | peruagor         | 1               |
| edentulus       | 1            | edentulum        | 1               |
| tonsus          | 1            | tondeo           | 1               |
| clausum         | 1            | claudo           | 1               |
| nomen           | 1            | nomine           | 1               |
| mendice         | 1            | mendicus         | 1               |
| senecta         | 1            | senectus         | 1               |
| sex             | 1            | uiginti          | 1               |
| undeuiginti     | 1            | uiginti          | 1               |
| aeneator        | 1            | aenator          | 1               |
| praetereo       | 1            | praeteritus      | 1               |
| euagor          | 1            | euago            | 1               |
| pomeridianus    | 1            | postmeridianus   | 1               |
| exprimo         | 1            | sum              | 1               |
| amestratini     | 1            | amestratinus     | 1               |
| luceria         | 1            | lucerius         | 1               |
| bouianum        | 1            | bouianus         | 1               |
| samnium         | 1            | samnius          | 1               |
| metropolitae    | 1            | metropolites     | 1               |
| gomphensis      | 1            | gomphenses       | 1               |
| pugilatus       | 1            | pugilo           | 1               |
| neratius        | 1            | nerates          | 1               |
| male            | 1            | malus            | 1               |
| seleucea        | 1            | seleuceus        | 1               |
| aequus          | 1            | aequum           | 1               |
| heracleon       | 1            | heracleus        | 1               |
| achilles        | 1            | achilleus        | 1               |
| praepositus     | 1            | praepono         | 1               |
| aboleo          | 1            | abolesco         | 1               |
| dedoleo         | 1            | dedolesco        | 1               |
| eneruo          | 1            | enerueo          | 1               |
| suspicio        | 1            | suspectus        | 1               |
| obsonium        | 1            | obsonio          | 1               |
| questus         | 1            | queror           | 1               |
| enitor          | 1            | eniteo           | 1               |
| carseoli        | 1            | carseolae        | 1               |
| oliuum          | 1            | oliuus           | 1               |
| paeligni        | 1            | paelignus        | 1               |
| panicum         | 1            | panicus          | 1               |
| corruptus       | 1            | corrumpo         | 1               |
| iliades         | 1            | ilias            | 1               |
| partus          | 1            | pario            | 1               |
| tribus          | 1            | tres             | 1               |
| plantaris       | 1            | plantarium       | 1               |
| carenus         | 1            | carenae          | 1               |
| urius           | 1            | urion            | 1               |
| uolcanus        | 1            | uulcanus         | 1               |
| andron          | 1            | andrus           | 1               |
| ab              | 1            | ah               | 1               |
| crudeliter      | 1            | crudelis         | 1               |
| oppidani        | 1            | oppidanus        | 1               |
| dirigo          | 1            | directus         | 1               |
| nuntio          | 1            | nuntius          | 1               |
| ludificor       | 1            | ludifico         | 1               |
| obsisto         | 1            | obsto            | 1               |
| contractus      | 1            | contraho         | 1               |
| iucundus        | 1            | iocundus         | 1               |
| impatientia     | 1            | impatiens        | 1               |
| consero         | 1            | conseuio         | 1               |
| mattiaci        | 1            | mattiacus        | 1               |
| incruentus      | 1            | incruens         | 1               |
| repleo          | 1            | repletus         | 1               |
| uito            | 1            | uitis            | 1               |
| conuiualis      | 1            | conuiualia       | 1               |
| auunculus       | 1            | auunculum        | 1               |
| onager          | 1            | onagrum          | 1               |
| uas             | 1            | uado             | 1               |
| auus            | 1            | auis             | 1               |
| pertimeo        | 1            | pertimesco       | 1               |
| inauratus       | 1            | inauro           | 1               |
| praesum         | 1            | praesens         | 1               |
| utrum           | 1            | uter             | 1               |
| praepinguis     | 1            | praepingue       | 1               |
| stagnans        | 1            | stagno           | 1               |
| quanto          | 1            | quantus          | 1               |
| reliqua         | 1            | reliquum         | 1               |
| thyias          | 1            | thyas            | 1               |
| trietericus     | 1            | trietericum      | 1               |
| anas            | 1            | ana              | 1               |
| foris           | 1            | sum              | 1               |
| regia           | 1            | regius           | 1               |
| pittacium       | 1            | pittacia         | 1               |
| africanus       | 1            | africani         | 1               |
| dardanis        | 1            | dardanides       | 1               |
| presso          | 1            | premo            | 1               |
| semotus         | 1            | semoueo          | 1               |
| consideratus    | 1            | considero        | 1               |
| statuo          | 1            | statua           | 1               |
| sophistes       | 1            | sophista         | 1               |
| mortarium       | 1            | mortarius        | 1               |
| latini          | 1            | latinus          | 1               |
| obnixus         | 1            | obnitor          | 1               |
| anhelo          | 1            | anhelus          | 1               |
| defetiscor      | 1            | sumitto          | 1               |
| hydraules       | 1            | hydraula         | 1               |
| fundatus        | 1            | fundo            | 1               |
| malefacio       | 1            | facio            | 1               |
| balantes        | 1            | balo             | 1               |
| cheruscus       | 1            | cherusca         | 1               |
| impercussus     | 1            | impercutio       | 1               |
| latruncularius  | 1            | latruncularia    | 1               |
| conuentum       | 1            | conuenio         | 1               |
| aequum          | 1            | aequus           | 1               |
| seligo          | 1            | selectum         | 1               |
| uere            | 1            | uerus            | 1               |
| priscus         | 1            | prisci           | 1               |
| muscipulum      | 1            | muscipulus       | 1               |
| quintus         | 1            | quinque          | 1               |
| sestertium      | 1            | sestertius       | 1               |
| ausonius        | 1            | ausonii          | 1               |
| troia           | 1            | troius           | 1               |
| pecco           | 1            | peccans          | 1               |
| orestae         | 1            | orestes          | 1               |
| lyncestae       | 1            | lyncesta         | 1               |
| sepositus       | 1            | sepono           | 1               |
| praesens        | 1            | praesum          | 1               |
| caelum          | 1            | coelum           | 1               |
| diuerto         | 1            | diuersus         | 1               |
| sciron          | 1            | sciro            | 1               |
| festum          | 1            | festus           | 1               |
| agatho          | 1            | agathon          | 1               |
| diligens        | 1            | diligo           | 1               |
| derdas          | 1            | derda            | 1               |
| libet           | 1            | libere           | 1               |
| monitus         | 1            | moneo            | 1               |
| penteremis      | 1            | penter           | 1               |
| dicrota         | 1            | dicrotus         | 1               |
| penso           | 1            | penseo           | 1               |
| sibylla         | 1            | sibulla          | 1               |
| aufilenus       | 1            | aufilenaus       | 1               |
| ueronensis      | 1            | ueronensus       | 1               |
| acratus         | 1            | acraton          | 1               |
| metuens         | 1            | metuo            | 1               |
| sino            | 1            | sine             | 1               |
| acesta          | 1            | acestes          | 1               |
| inaratus        | 1            | inaro            | 1               |
| promulsidare    | 1            | promulsido       | 1               |
| bissacius       | 1            | bisaccium        | 1               |
| luno            | 1            | lunatus          | 1               |
| ea              | 1            | is               | 1               |
| niteo           | 1            | nitueo           | 1               |
| phoenice        | 1            | phoenices        | 1               |
| intestinus      | 1            | intestinum       | 1               |
| cluuiae         | 1            | cluuius          | 1               |
| resto           | 1            | resisto          | 1               |
| liburnus        | 1            | liburna          | 1               |
| sexagesimus     | 1            | sexaginta        | 1               |
| transrhenanus   | 1            | transrhenani     | 1               |
| loricatus       | 1            | lorico           | 1               |
| tuder           | 1            | tudris           | 1               |
| externus        | 1            | externi          | 1               |
| proxime         | 1            | prope            | 1               |
| merens          | 1            | mereor           | 1               |
| obsero          | 1            | obsiuisco        | 1               |
| tyro            | 1            | tyrus            | 1               |
| alcyone         | 1            | alcyon           | 1               |
| ceyce           | 1            | ceyx             | 1               |
| aueon           | 1            | aueone           | 1               |
| laodice         | 1            | laodicus         | 1               |
| uermino         | 1            | uerminor         | 1               |
| quintum         | 1            | quintus          | 1               |
| oppidanus       | 1            | oppidani         | 1               |
| clusium         | 1            | clusus           | 1               |
| corytus         | 1            | gorytus          | 1               |
| praeparatus     | 1            | praeparo         | 1               |
| lautumiae       | 1            | latomia          | 1               |
| fio             | 1            | fiaesus          | 1               |
| ida             | 1            | ide              | 1               |
| traho           | 1            | tractus          | 1               |
| orior           | 1            | ortus            | 1               |
| hermeros        | 1            | hermerotus       | 1               |
| naualis         | 1            | naualia          | 1               |
| iuror           | 1            | iuratus          | 1               |
| nauis           | 1            | nauus            | 1               |
| scipiadas       | 1            | scipiades        | 1               |
| camera          | 1            | camarus          | 1               |
| sucinum         | 1            | sucina           | 1               |
| pila            | 1            | pilum            | 1               |
| coniunctum      | 1            | coniunctus       | 1               |
| segrego         | 1            | grego            | 1               |
| latiaris        | 1            | latiarius        | 1               |
| paruum          | 1            | paruus           | 1               |
| datum           | 1            | do               | 1               |
| clipeus         | 1            | clupeus          | 1               |
| uolsella        | 1            | uulsella         | 1               |
| pecten          | 1            | pecto            | 1               |
| calamistrum     | 1            | calamister       | 1               |
| tempestiuo      | 1            | tempestiuus      | 1               |
| defungor        | 1            | defunctus        | 1               |
| caligarius      | 1            | caligarium       | 1               |
| troius          | 1            | troia            | 1               |
| carex           | 1            | carix            | 1               |
| artifex         | 1            | artificium       | 1               |
| siremps         | 1            | sirempe          | 1               |
| taciturnus      | 1            | taciturne        | 1               |
| compareo        | 1            | comparens        | 1               |
| pythagoreus     | 1            | pythagorei       | 1               |
| exopto          | 1            | exoptatus        | 1               |
| nymphaeum       | 1            | nymphaeus        | 1               |
| inchoo          | 1            | incoho           | 1               |
| superfundo      | 1            | fundo            | 1               |
| mendax          | 1            | mendacium        | 1               |
| recuruus        | 1            | recurus          | 1               |
| culta           | 1            | colo             | 1               |
| crustumeri      | 1            | crustumerus      | 1               |
| antemnae        | 1            | antemna          | 1               |
| uulua           | 1            | uolua            | 1               |
| lupanar         | 1            | lupanaris        | 1               |
| assisto         | 1            | asto             | 1               |
| consequor       | 1            | consequens       | 1               |
| osci            | 1            | oscus            | 1               |
| sarmentus       | 1            | sarmentum        | 1               |
| dardani         | 1            | dardanis         | 1               |
| axicia          | 1            | axitium          | 1               |
| extersus        | 1            | extergeo         | 1               |
| quadragiens     | 1            | quadragies       | 1               |
| cylleneus       | 1            | cyllenius        | 1               |
| panaetius       | 1            | panaetus         | 1               |
| dilectus        | 1            | diligo           | 1               |
| maerens         | 1            | maereo           | 1               |
| concupisco      | 1            | concupitus       | 1               |
| circumspecto    | 1            | specto           | 1               |
| palilia         | 1            | palilius         | 1               |
| saturnia        | 1            | saturnius        | 1               |
| scamnum         | 1            | scamnus          | 1               |
| rutulus         | 1            | rutuli           | 1               |
| barzaentes      | 1            | barzaentus       | 1               |
| collare         | 1            | collaris         | 1               |
| deico           | 1            | deicio           | 1               |
| honesto         | 1            | honestus         | 1               |
| conuinco        | 1            | conuictus        | 1               |
| uictoriatus     | 1            | uictorior        | 1               |
| uulchalo        | 1            | uulchalon        | 1               |
| cobiamachus     | 1            | cobiomagus       | 1               |
| chiliarches     | 1            | chiliarchae      | 1               |
| mazagae         | 1            | mazages          | 1               |
| cleophis        | 1            | cleophi          | 1               |
| alte            | 1            | altus            | 1               |
| cerealis        | 1            | cerialis         | 1               |
| concorditer     | 1            | concorde         | 1               |
| asporto         | 1            | asporqueo        | 1               |
| contremisco     | 1            | contremo         | 1               |
| gaia            | 1            | gaiae            | 1               |
| eurytides       | 1            | eurytis          | 1               |
| lepor           | 1            | lepus            | 1               |
| inuerencundus   | 1            | inuerecundus     | 1               |
| promoueo        | 1            | promoro          | 1               |
| reuocamen       | 1            | reuoco           | 1               |
| minutal         | 1            | minutalis        | 1               |
| barcanus        | 1            | barcani          | 1               |
| refutatus       | 1            | refuto           | 1               |
| iussum          | 1            | iubeo            | 1               |
| mnestheus       | 1            | mnesthea         | 1               |
| rimor           | 1            | rimatus          | 1               |
| deferueo        | 1            | deferuesco       | 1               |
| numatus         | 1            | nummatus         | 1               |
| fluuidus        | 1            | fluidus          | 1               |
| nupta           | 1            | nubo             | 1               |
| permano         | 1            | permaneo         | 1               |
| bellatulus      | 1            | belliatulum      | 1               |
| ueto            | 1            | uetuus           | 1               |
| modico          | 1            | modicus          | 1               |
| granarium       | 1            | granarius        | 1               |
| emolo           | 1            | emoleo           | 1               |
| aricini         | 1            | aricinus         | 1               |
| laurentes       | 1            | laurens          | 1               |
| conuenio        | 1            | conueniens       | 1               |
| obuiam          | 1            | obuia            | 1               |
| cyathus         | 1            | cyatus           | 1               |
| centussis       | 1            | centusse         | 1               |
| irascor         | 1            | iratus           | 1               |
| aeditumus       | 1            | aeditum          | 1               |
| compitalia      | 1            | compitalis       | 1               |
| prosecta        | 1            | proseco          | 1               |
| adhaereo        | 1            | adhaeresco       | 1               |
| braca           | 1            | bracus           | 1               |
| uinum           | 1            | uinipollens      | 1               |
| pollens         | 1            | uinipollens      | 1               |
| esculentus      | 1            | esculeor         | 1               |
| redoleo         | 1            | redolens         | 1               |
| specula         | 1            | speculum         | 1               |
| obligo          | 1            | obligatus        | 1               |
| incipio         | 1            | inceptum         | 1               |
| quodammodo      | 1            | quidammodus      | 1               |
| lente           | 1            | lentus           | 1               |
| balnearia       | 1            | balinarium       | 1               |
| expolio         | 1            | expolo           | 1               |
| numulariolus    | 1            | nummulariolus    | 1               |
| uictus          | 1            | uinco            | 1               |
| hei             | 1            | ei               | 1               |
| flecto          | 1            | flexura          | 1               |
| echo            | 1            | echus            | 1               |
| parata          | 1            | paratus          | 1               |
| obscurum        | 1            | obscurus         | 1               |
| constratum      | 1            | consterno        | 1               |
| pampinus        | 1            | pampina          | 1               |
| arcadia         | 1            | arcadius         | 1               |
| proprium        | 1            | proprius         | 1               |
| siluester       | 1            | siluestris       | 1               |
| astrictus       | 1            | astringo         | 1               |
| collectus       | 1            | colligo          | 1               |
| philippi        | 1            | philippus        | 1               |
| deuotus         | 1            | deuoueo          | 1               |
| obtusus         | 1            | obtunsus         | 1               |
| libo            | 1            | libet            | 1               |
| uenalis         | 1            | uenales          | 1               |
| confluens       | 1            | confluo          | 1               |
| sybylla         | 1            | sibylla          | 1               |
| erectus         | 1            | erigo            | 1               |
| epistomium      | 1            | epitonia         | 1               |
| occurro         | 1            | occursus         | 1               |
| sophene         | 1            | sophenes         | 1               |
| ambiguum        | 1            | ambiguus         | 1               |
| seuera          | 1            | seuerus          | 1               |
| nobilitas       | 1            | nobilito         | 1               |
| clitus          | 1            | clitius          | 1               |
| pedanus         | 1            | pedana           | 1               |
| euans           | 1            | euantus          | 1               |
| sitiens         | 1            | sitio            | 1               |
| attalus         | 1            | attalius         | 1               |
| alo             | 1            | altus            | 1               |
| nuntius         | 1            | nuntium          | 1               |
| thucidides      | 1            | thucydis         | 1               |
| longe           | 1            | longus           | 1               |
| procerus        | 1            | procer           | 1               |
| abditus         | 1            | abdo             | 1               |
| curo            | 1            | cura             | 1               |
| plancus         | 1            | plancius         | 1               |
| nato            | 1            | nator            | 1               |
| uicina          | 1            | uicinus          | 1               |
| iuuentius       | 1            | iuuentii         | 1               |
| discessus       | 1            | discedo          | 1               |
| exspectatus     | 1            | exspecto         | 1               |
| corculum        | 1            | corculus         | 1               |
| incensus        | 1            | incendo          | 1               |
| remoueo         | 1            | remotus          | 1               |
| nisus           | 1            | nixus            | 1               |
| cephenes        | 1            | cephenus         | 1               |
| acceptum        | 1            | accipio          | 1               |
| bubulus         | 1            | bublum           | 1               |
| pilatus         | 1            | pilates          | 1               |
| nonaginta       | 1            | uiginti          | 1               |
| fornacula       | 1            | fornaculum       | 1               |
| horreo          | 1            | horrens          | 1               |
| secundani       | 1            | secundanus       | 1               |
| for             | 1            | farior           | 1               |
| pegma           | 1            | pegmatum         | 1               |
| deliculus       | 1            | deliculum        | 1               |
| retinens        | 1            | retineo          | 1               |
| conscribo       | 1            | conscriptor      | 1               |
| paco            | 1            | pacatus          | 1               |
| tusculanus      | 1            | tusculani        | 1               |
| tiburtinus      | 1            | tiburtini        | 1               |
| praenestinus    | 1            | praenestini      | 1               |
| creo            | 1            | creetus          | 1               |
| fluens          | 1            | fluo             | 1               |
| fraus           | 1            | fraudium         | 1               |
| biiugus         | 1            | biiugi           | 1               |
| pendeo          | 1            | pendo            | 1               |
| anima           | 1            | animus           | 1               |
| translaticius   | 1            | translatius      | 1               |
| exsero          | 1            | exereo           | 1               |
| elesioduli      | 1            | elesiodulae      | 1               |
| pileum          | 1            | pileus           | 1               |
| sipho           | 1            | sipus            | 1               |
| propago         | 1            | propages         | 1               |
| conecto         | 1            | connecto         | 1               |
| profugio        | 1            | profugus         | 1               |
| uello           | 1            | uellus           | 1               |
| aestiua         | 1            | aestiuus         | 1               |
| mille           | 1            | quingenti        | 1               |
| argo            | 1            | argus            | 1               |
| pudeo           | 1            | pudendus         | 1               |
| meritorius      | 1            | meritorium       | 1               |
| distendo        | 1            | distentus        | 1               |
| egero           | 1            | ago              | 1               |
| turbatus        | 1            | turbo            | 1               |
| seueri          | 1            | seuerus          | 1               |
| carpus          | 1            | carpe            | 1               |
| consul          | 1            | consulo          | 1               |
| riuulus         | 1            | riuolus          | 1               |
| morum           | 1            | mos              | 1               |
| ionium          | 1            | ionius           | 1               |
| postilla        | 1            | postillus        | 1               |
| ionius          | 1            | hionius          | 1               |
| stratonica      | 1            | stratonicus      | 1               |
| epigonus        | 1            | epigones         | 1               |
| morator         | 1            | moratus          | 1               |
| expendo         | 1            | expensum         | 1               |
| uestio          | 1            | uestitus         | 1               |
| lauo            | 1            | lautus           | 1               |
| stulti          | 1            | stultus          | 1               |
| ortus           | 1            | orior            | 1               |
| pictus          | 1            | pingo            | 1               |
| summula         | 1            | submula          | 1               |
| aemulus         | 1            | aemula           | 1               |
| thraca          | 1            | thraces          | 1               |
| epulo           | 1            | epulon           | 1               |
| aemulatus       | 1            | aemulor          | 1               |
| pauca           | 1            | paucus           | 1               |
| abauus          | 1            | abaui            | 1               |
| satrapea        | 1            | satrapeus        | 1               |
| sardes          | 1            | sardius          | 1               |
| genitalia       | 1            | genitalis        | 1               |
| debitum         | 1            | debeo            | 1               |
| celebratus      | 1            | celebro          | 1               |
| circenses       | 1            | circensis        | 1               |
| saturnius       | 1            | saturnia         | 1               |
| postquam        | 1            | quam             | 1               |
| tiberis         | 1            | tiberius         | 1               |
| ptolemaeus      | 1            | ptolomaeus       | 1               |
| fulcio          | 1            | fultus           | 1               |
| adaugeo         | 1            | adaugo           | 1               |
| confercio       | 1            | confertus        | 1               |
| hospitus        | 1            | hospita          | 1               |
| rigens          | 1            | rigeo            | 1               |
| inuito          | 1            | inuitus          | 1               |
| excetra         | 1            | excetro          | 1               |
| uigil           | 1            | uigiles          | 1               |
| nitens          | 1            | nitor            | 1               |
| uerto           | 1            | uersus           | 1               |
| oppedo          | 1            | oppedio          | 1               |
| suspendo        | 1            | suspensus        | 1               |
| concursus       | 1            | consurgo         | 1               |
| adiectus        | 1            | adicio           | 1               |
| uter            | 1            | utrum            | 1               |
| decresco        | 1            | decerno          | 1               |
| pedo            | 1            | pedones          | 1               |
| mens            | 1            | mentius          | 1               |
| conor           | 1            | conatus          | 1               |
| repetundae      | 1            | repeto           | 1               |
| crusta          | 1            | crustum          | 1               |
| merges          | 1            | mergo            | 1               |
| gryneus         | 1            | grynus           | 1               |
| caelestis       | 1            | caelestia        | 1               |
| consulto        | 1            | consultum        | 1               |
| intercolumnium  | 1            | intercolumnialum | 1               |
| lanuuium        | 1            | lanuuius         | 1               |
| hiberia         | 1            | iberiia          | 1               |
| pannucia        | 1            | pannucius        | 1               |
| desideo         | 1            | desido           | 1               |
| libro           | 1            | liber            | 1               |
| septuaginta     | 1            | duo              | 1               |
| aduolo          | 1            | aduola           | 1               |
| auenticum       | 1            | auenticus        | 1               |
| agaso           | 1            | agasonis         | 1               |
| uinco           | 1            | uictus           | 1               |
| damnatus        | 1            | damno            | 1               |
| pauimentatus    | 1            | pauimento        | 1               |
| thyiades        | 1            | thyias           | 1               |
| quadriduum      | 1            | quadriduus       | 1               |
| albanus         | 1            | albani           | 1               |
| setinus         | 1            | setini           | 1               |
| contemno        | 1            | contemptus       | 1               |
| iulius          | 1            | iulia            | 1               |
| obscena         | 1            | obscenum         | 1               |
| auersus         | 1            | auerto           | 1               |
| triuia          | 1            | triuiaus         | 1               |
| parrhasis       | 1            | parrhasides      | 1               |
| leontini        | 1            | leontinus        | 1               |
| crystallina     | 1            | crustallina      | 1               |
| damno           | 1            | damnum           | 1               |
| quonam          | 1            | quisnam          | 1               |
| suauiter        | 1            | suauis           | 1               |
| diuerbium       | 1            | deuerbium        | 1               |
| uenditum        | 1            | uendo            | 1               |
| amastriani      | 1            | amastrianus      | 1               |
| cadmeius        | 1            | cadmeus          | 1               |
| lues            | 1            | luo              | 1               |
| diserte         | 1            | disertus         | 1               |
| scelerate       | 1            | sceleratus       | 1               |
| fruticetum      | 1            | fruticeo         | 1               |
| tectus          | 1            | tego             | 1               |
| ecclesia        | 1            | ecclesius        | 1               |
| leonidas        | 1            | leonida          | 1               |
| uireo           | 1            | uirens           | 1               |
| conuicior       | 1            | conuicio         | 1               |
| uindico         | 1            | uindex           | 1               |
| simulus         | 1            | simula           | 1               |
| satyra          | 1            | satura           | 1               |
| turonus         | 1            | turones          | 1               |
| treuir          | 1            | treuirus         | 1               |
| distinguo       | 1            | distinctus       | 1               |
| exsolutio       | 1            | exsoltio         | 1               |
| magnificens     | 1            | magnificus       | 1               |
| obsoletus       | 1            | obsolesco        | 1               |
| polluceo        | 1            | pollugo          | 1               |
| qualum          | 1            | qualus           | 1               |
| cytherea        | 1            | cythereus        | 1               |
| pingue          | 1            | pinguis          | 1               |
| argentaria      | 1            | argentarius      | 1               |
| auxiliaris      | 1            | auxiliares       | 1               |
| libero          | 1            | liber            | 1               |
| migro           | 1            | migrus           | 1               |
| ambiuareti      | 1            | ambiuariti       | 1               |
| laeua           | 1            | laeuus           | 1               |
| corinthii       | 1            | corinthius       | 1               |
| nasum           | 1            | nasus            | 1               |
| arripio         | 1            | abripio          | 1               |
| quicumque       | 1            | qui              | 1               |
| uocito          | 1            | uocites          | 1               |
| distentus       | 1            | distineo         | 1               |
| martius         | 1            | marsicus         | 1               |
| subicio         | 1            | subiectus        | 1               |
| coniunctus      | 1            | coniungo         | 1               |
| clodia          | 1            | clodius          | 1               |
| praesaepe       | 1            | praesepe         | 1               |
| sine            | 1            | sino             | 1               |
| submissus       | 1            | submitto         | 1               |
| cunctor         | 1            | conto            | 1               |
| moscillus       | 1            | moscillum        | 1               |
| heroum          | 1            | herous           | 1               |
| aphidnae        | 1            | aphidnas         | 1               |
| reliqui         | 1            | reliquus         | 1               |
| hannibal        | 1            | annibalis        | 1               |
| crotoniates     | 1            | crotoniata       | 1               |
| pungo           | 1            | punctum          | 1               |
| umbrosa         | 1            | umbrosus         | 1               |
| ualeo           | 1            | ualea            | 1               |
| transigo        | 1            | tansactus        | 1               |
| pergrauis       | 1            | praegrauis       | 1               |
| exercitatus     | 1            | exercito         | 1               |
| centumuiralis   | 1            | cuiralis         | 1               |
| serium          | 1            | serius           | 1               |
| dextera         | 1            | dexter           | 1               |
| pars            | 1            | pario            | 1               |
| marita          | 1            | maritus          | 1               |
| septimus        | 1            | septem           | 1               |
| idus            | 1            | idferior         | 1               |
| dispendium      | 1            | dispendo         | 1               |
| apophoreta      | 1            | apophoretum      | 1               |
| facile          | 1            | facilis          | 1               |
| gymnasium       | 1            | gymnasus         | 1               |
| delenio         | 1            | delinio          | 1               |
| auspicor        | 1            | auspicatus       | 1               |
| tantusdem       | 1            | tantumdem        | 1               |
| bulla           | 1            | bullum           | 1               |
| euterpe         | 1            | euterpus         | 1               |
| germanus        | 1            | germani          | 1               |
| grauis          | 1            | grauiter         | 1               |
| aeque           | 1            | aequus           | 1               |
| mattea          | 1            | matteus          | 1               |
| obticesco       | 1            | obticeo          | 1               |
| babaecalus      | 1            | babaecalis       | 1               |
| aliquo          | 1            | aliquis          | 1               |
| uaria           | 1            | uarius           | 1               |
| maxilla         | 1            | maxillum         | 1               |
| gausapum        | 1            | gausape          | 1               |
| gurgulio        | 1            | gurgulium        | 1               |
| paulus          | 1            | pauli            | 1               |
| sto             | 1            | statura          | 1               |
| sestertius      | 1            | sestertium       | 1               |
| praeneste       | 1            | praenestus       | 1               |
| auertor         | 1            | auerto           | 1               |
| monstrum        | 1            | monstro          | 1               |
| oricalchum      | 1            | orichalcum       | 1               |
| imperatum       | 1            | impero           | 1               |
| tener           | 1            | teneo            | 1               |
| sacratus        | 1            | sacro            | 1               |
| tiburtius       | 1            | tiburs           | 1               |
| tiburtus        | 1            | tiburs           | 1               |
| monstro         | 1            | monstrum         | 1               |
| scateo          | 1            | scato            | 1               |
| sexcenti        | 1            | sescenti         | 1               |
| colus           | 1            | colo             | 1               |
| scribonius      | 1            | scribo           | 1               |
| tarpezita       | 1            | trapezita        | 1               |
| aquifolius      | 1            | acrufolium       | 1               |
| amphitrite      | 1            | amphitrites      | 1               |
| ales            | 1            | alis             | 1               |
| istuc           | 1            | istic            | 1               |
| paphlagona      | 1            | paphlagones      | 1               |
| sinopa          | 1            | sinopes          | 1               |
| arabes          | 1            | arabs            | 1               |
| cara            | 1            | cares            | 1               |
| cretanus        | 1            | cretani          | 1               |
| rhodia          | 1            | rhodius          | 1               |
| unomammius      | 1            | unomammia        | 1               |
| conterebromnius | 1            | conterebromia    | 1               |
| atalante        | 1            | atalas           | 1               |
| no              | 1            | nassis           | 1               |
| calesco         | 1            | caleo            | 1               |
| doceo           | 1            | doctus           | 1               |
| subtexo         | 1            | subtego          | 1               |
| perfrigesco     | 1            | perfrigo         | 1               |
| cichorium       | 1            | cichoreus        | 1               |
| nimium          | 1            | nimius           | 1               |
| asprenates      | 1            | asprenas         | 1               |
| tertio          | 1            | tertius          | 1               |
| eminens         | 1            | emineo           | 1               |
| inexsuperabilis | 1            | inexsuperbilis   | 1               |
| detergeo        | 1            | detergo          | 1               |
| boeotus         | 1            | boeota           | 1               |
| insido          | 1            | insideo          | 1               |
| germana         | 1            | germanus         | 1               |
| noti            | 1            | notus            | 1               |
| sauium          | 1            | suauium          | 1               |
| cognosco        | 1            | cognitus         | 1               |
| incelebratus    | 1            | incelebro        | 1               |
| reflo           | 1            | refero           | 1               |
| pontius         | 1            | pontus           | 1               |
| infectus        | 1            | inficio          | 1               |
| assarius        | 1            | assaria          | 1               |
| separo          | 1            | separatus        | 1               |
| quies           | 1            | quietus          | 1               |
| codex           | 1            | caudex           | 1               |
| creber          | 1            | crebior          | 1               |
| pelasgus        | 1            | pelasgi          | 1               |
| cena            | 1            | ceno             | 1               |
| tyrrhenus       | 1            | tyrrhene         | 1               |
| timidus         | 1            | timide           | 1               |
| tyrannus        | 1            | tyrannes         | 1               |
| heracleotae     | 1            | heracleotarus    | 1               |
| singula         | 1            | singulus         | 1               |
| confundo        | 1            | confusus         | 1               |
| lucus           | 1            | lux              | 1               |
| eiuro           | 1            | eiurum           | 1               |
| comitor         | 1            | comitatus        | 1               |
| refoueo         | 1            | refo             | 1               |
| laeuum          | 1            | laeuus           | 1               |
| situs           | 1            | sino             | 1               |
| prouoco         | 1            | prouoca          | 1               |
| ariarathes      | 1            | ariarathus       | 1               |
| uacillo         | 1            | uaccillo         | 1               |
| ubius           | 1            | ubii             | 1               |
| samnis          | 1            | samnites         | 1               |
| bellum          | 1            | duellum          | 1               |
| turda           | 1            | turdus           | 1               |
| rutilus         | 1            | rutulus          | 1               |
| usus            | 1            | utor             | 1               |
| spondeo         | 1            | sponsa           | 1               |
| relinquo        | 1            | reliquum         | 1               |
| teleboae        | 1            | teleboa          | 1               |
| matula          | 1            | matulus          | 1               |
| serenus         | 1            | serenum          | 1               |
| sponsus         | 1            | sponsum          | 1               |
| ludifico        | 1            | ludificor        | 1               |
| rectum          | 1            | rectus           | 1               |
| morbus          | 1            | morbi            | 1               |
| quantulum       | 1            | quantulus        | 1               |
| clandestino     | 1            | clandestinus     | 1               |
| oppositus       | 1            | oppono           | 1               |
| lemniscatus     | 1            | lemniscor        | 1               |
| ictus           | 1            | ico              | 1               |
| secedo          | 1            | secessum         | 1               |
| nesis           | 1            | nesida           | 1               |
| grauiter        | 1            | grauis           | 1               |
| commissum       | 1            | committo         | 1               |
| scelerati       | 1            | sceleratus       | 1               |
| aduenticium     | 1            | aduenticius      | 1               |
| quiuis          | 1            | quis             | 1               |
| uergiliae       | 1            | uergilia         | 1               |
| etiamtunc       | 1            | etiamtum         | 1               |
| ruscum          | 1            | ruscus           | 1               |
| proiectus       | 1            | proicio          | 1               |
| alga            | 1            | algo             | 1               |
| irretio         | 1            | irreto           | 1               |
| somnior         | 1            | somnio           | 1               |
| sarisa          | 1            | sarissus         | 1               |
| longinquum      | 1            | longinquus       | 1               |
| clathratus      | 1            | clatratus        | 1               |
| mensis          | 1            | mensa            | 1               |
| reginus         | 1            | regini           | 1               |
| etruscus        | 1            | etrusci          | 1               |
| caerulus        | 1            | caeruleus        | 1               |
| itali           | 1            | italus           | 1               |
| destinatus      | 1            | destino          | 1               |
| atreus          | 1            | atrea            | 1               |
| reuerto         | 1            | reuertor         | 1               |
| merum           | 1            | merus            | 1               |
| deuito          | 1            | deues            | 1               |
| agyrium         | 1            | agyrus           | 1               |
| libenter        | 1            | libens           | 1               |
| fixus           | 1            | figo             | 1               |
| matertera       | 1            | materter         | 1               |
| quatuor         | 1            | trecenti         | 1               |
| sors            | 1            | sortio           | 1               |
| incommodus      | 1            | incommodum       | 1               |
| mare            | 1            | maris            | 1               |
| iaceo           | 1            | iacio            | 1               |
| uilis           | 1            | uile             | 1               |
| luminare        | 1            | luminarium       | 1               |
| paululus        | 1            | paulula          | 1               |
| fullonius       | 1            | fullonia         | 1               |
| abscido         | 1            | abscindo         | 1               |
| dira            | 1            | dirus            | 1               |
| cesso           | 1            | cessum           | 1               |
| galesus         | 1            | galaesus         | 1               |
| attritus        | 1            | attero           | 1               |
| daphnis         | 1            | daphnin          | 1               |
| ringor          | 1            | ringo            | 1               |
| audentia        | 1            | audens           | 1               |
| pango           | 1            | pactum           | 1               |
| opertus         | 1            | operio           | 1               |
| rosetum         | 1            | roso             | 1               |
| egregium        | 1            | egregius         | 1               |
| ualentulus      | 1            | sum              | 1               |
| agito           | 1            | ago              | 1               |
| compendiaria    | 1            | compendiarium    | 1               |
| iuuo            | 1            | eo               | 1               |
| censeo          | 1            | census           | 1               |
| deuexus         | 1            | deueho           | 1               |
| aruina          | 1            | aruinum          | 1               |
| notabilis       | 1            | notabiliter      | 1               |
| affatus         | 1            | affor            | 1               |
| gregales        | 1            | gregalis         | 1               |
| cous            | 1            | coi              | 1               |
| tmolites        | 1            | tmolitae         | 1               |
| phalacrus       | 1            | phalacrys        | 1               |
| pransus         | 1            | prandeo          | 1               |
| testor          | 1            | testatus         | 1               |
| menta           | 1            | maeta            | 1               |
| conuerso        | 1            | conuerto         | 1               |
| eros            | 1            | erotus           | 1               |
| repulsa         | 1            | repello          | 1               |
| compsani        | 1            | compsanus        | 1               |
| symplegas       | 1            | symplegades      | 1               |
| secerno         | 1            | secretus         | 1               |
| deicio          | 1            | sum              | 1               |
| uenor           | 1            | uenatus          | 1               |
| prudens         | 1            | prudenter        | 1               |
| ligellum        | 1            | ligellus         | 1               |
| liris           | 1            | lir              | 1               |
| abiectus        | 1            | abicio           | 1               |
| desertum        | 1            | desero           | 1               |
| patiens         | 1            | patior           | 1               |
| tapetum         | 1            | tapes            | 1               |
| nouus           | 1            | nosco            | 1               |
| uiso            | 1            | uideo            | 1               |
| apertum         | 1            | apertus          | 1               |
| receptum        | 1            | recipio          | 1               |
| castaneus       | 1            | castanea         | 1               |
| prunum          | 1            | pruna            | 1               |
| occulo          | 1            | occultus         | 1               |
| cauponor        | 1            | caupono          | 1               |
| treuirus        | 1            | treuiri          | 1               |
| fuco            | 1            | fucatus          | 1               |
| rictum          | 1            | rictus           | 1               |
| obscurus        | 1            | obscurum         | 1               |
| oneratus        | 1            | onero            | 1               |
| accommodo       | 1            | accommodatus     | 1               |
| caesarianus     | 1            | caesariani       | 1               |
| sura            | 1            | syra             | 1               |
| aluntium        | 1            | haluntus         | 1               |
| corinthium      | 1            | corinthius       | 1               |
| quasso          | 1            | quatio           | 1               |
| torua           | 1            | toruus           | 1               |
| interdatus      | 1            | interdo          | 1               |
| micans          | 1            | mico             | 1               |
| ambeo           | 1            | ambio            | 1               |
| duodenus        | 1            | duodeni          | 1               |
| maneo           | 1            | manes            | 1               |
| sorbum          | 1            | sorbus           | 1               |
| hospita         | 1            | hospitus         | 1               |
| exigo           | 1            | exactus          | 1               |
| uicesimus       | 1            | uicesis          | 1               |
| extergeo        | 1            | extersum         | 1               |
| praegressus     | 1            | praegredior      | 1               |
| euthymia        | 1            | euthymian        | 1               |
| horrendum       | 1            | horrendus        | 1               |
| latina          | 1            | latinus          | 1               |
| unguis          | 1            | ungo             | 1               |
| oculus          | 1            | oculeus          | 1               |
| profor          | 1            | profo            | 1               |
| perficio        | 1            | perfectus        | 1               |
| bifariam        | 1            | bifaria          | 1               |
| experior        | 1            | expers           | 1               |
| utroque         | 1            | uterque          | 1               |
| propero         | 1            | properans        | 1               |
| discolorius     | 1            | discoloris       | 1               |
| glesum          | 1            | gledo            | 1               |
| argei           | 1            | argeus           | 1               |
| saeptum         | 1            | saepio           | 1               |
| pharmacus       | 1            | pharmaces        | 1               |
| ampelus         | 1            | ampelon          | 1               |
| periurium       | 1            | periurus         | 1               |
| continuus       | 1            | contineo         | 1               |
| turbo           | 1            | turbatus         | 1               |
| campestria      | 1            | campester        | 1               |
| daunius         | 1            | daunia           | 1               |
| heraclius       | 1            | heracles         | 1               |
| secreto         | 1            | secretus         | 1               |
| uenia           | 1            | uenio            | 1               |
| exsilium        | 1            | exilis           | 1               |
| assimulo        | 1            | assimilo         | 1               |
| functus         | 1            | fungor           | 1               |
| pater           | 1            | publius          | 1               |
| macero          | 1            | macio            | 1               |
| istic           | 1            | istuc            | 1               |
| effectus        | 1            | efficio          | 1               |
| optimus         | 1            | bonus            | 1               |
| gangarides      | 1            | gangaridus       | 1               |
| coi             | 1            | cous             | 1               |
| periurus        | 1            | perur            | 1               |
| languens        | 1            | langueo          | 1               |
| cooperio        | 1            | copero           | 1               |
| comedo          | 1            | comesto          | 1               |
| iacio           | 1            | iaceo            | 1               |
| subsulto        | 1            | sussultus        | 1               |
| suscito         | 1            | suscio           | 1               |
| uarium          | 1            | uarius           | 1               |
| idolum          | 1            | idolon           | 1               |
| promissus       | 1            | promitto         | 1               |
| compedes        | 1            | compes           | 1               |
| helleborum      | 1            | helleborus       | 1               |
| scammonium      | 1            | scamonium        | 1               |
| appono          | 1            | appositus        | 1               |
| aricinus        | 1            | aricina          | 1               |
| mutinensis      | 1            | mutinensia       | 1               |
| hypsipyle       | 1            | hypsipylas       | 1               |
| consecue        | 1            | consecus         | 1               |
| purgatus        | 1            | purgo            | 1               |
| nihilum         | 1            | nilis            | 1               |
| latens          | 1            | lateo            | 1               |
| spumans         | 1            | spumo            | 1               |
| merga           | 1            | mergus           | 1               |
| fistuca         | 1            | festuca          | 1               |
| arpi            | 1            | arpus            | 1               |
| nautici         | 1            | nauticus         | 1               |
| tritus          | 1            | tero             | 1               |
| pancration      | 1            | pancratio        | 1               |

# POS

[Back to index](#index)

```
all:
  accuracy: 0.9706
  precision: 0.9215
  recall: 0.9139
  support: 170166
ambiguous-tokens:
  accuracy: 0.9228
  precision: 0.8745
  recall: 0.8536
  support: 53991
unknown-tokens:
  accuracy: 0.9363
  precision: 0.5289
  recall: 0.5039
  support: 5916
```

| Expected   | Total Errors | Predictions | Predicted times |
|------------|--------------|-------------|-----------------|
| ADJqua     | 915          | NOMcom      | 466             |
|            |              | VER         | 323             |
|            |              | ADV         | 109             |
|            |              | CONcoo      | 7               |
|            |              | PRE         | 6               |
|            |              | ADJord      | 2               |
|            |              | ADVint      | 1               |
|            |              | ADJdis      | 1               |
| NOMcom     | 907          | ADJqua      | 552             |
|            |              | VER         | 232             |
|            |              | ADV         | 47              |
|            |              | PROind      | 23              |
|            |              | PROpos.ref  | 12              |
|            |              | ADJcar      | 10              |
|            |              | NOMpro      | 8               |
|            |              | CONcoo      | 7               |
|            |              | ADJord      | 6               |
|            |              | PROpos      | 5               |
|            |              | PRE         | 1               |
|            |              | INJ         | 1               |
|            |              | PROper      | 1               |
|            |              | ADJadv.mul  | 1               |
|            |              | ADJdis      | 1               |
| ADV        | 554          | CONcoo      | 168             |
|            |              | ADJqua      | 101             |
|            |              | PROdem      | 96              |
|            |              | PRE         | 62              |
|            |              | NOMcom      | 43              |
|            |              | CONsub      | 26              |
|            |              | PROind      | 25              |
|            |              | VER         | 10              |
|            |              | ADVrel      | 9               |
|            |              | ADJcar      | 7               |
|            |              | ADVneg      | 2               |
|            |              | PROrel      | 2               |
|            |              | ADVint.neg  | 2               |
|            |              | ADJadv.mul  | 1               |
| VER        | 500          | ADJqua      | 246             |
|            |              | NOMcom      | 211             |
|            |              | CONsub      | 12              |
|            |              | ADV         | 10              |
|            |              | PROdem      | 5               |
|            |              | PRE         | 4               |
|            |              | ADVrel      | 4               |
|            |              | ADJcar      | 2               |
|            |              | INJ         | 2               |
|            |              | NOMpro      | 2               |
|            |              | ADVneg      | 1               |
|            |              | PROind      | 1               |
| CONsub     | 441          | ADVrel      | 167             |
|            |              | PROrel      | 118             |
|            |              | PRE         | 56              |
|            |              | CONcoo      | 34              |
|            |              | ADVneg      | 24              |
|            |              | ADVint      | 21              |
|            |              | ADV         | 16              |
|            |              | VER         | 4               |
|            |              | PROref      | 1               |
| PROrel     | 286          | PROint      | 91              |
|            |              | ADVrel      | 86              |
|            |              | CONsub      | 81              |
|            |              | ADVint      | 13              |
|            |              | PROind      | 12              |
|            |              | CONcoo      | 3               |
| ADVrel     | 241          | CONsub      | 137             |
|            |              | ADVint      | 51              |
|            |              | PROrel      | 44              |
|            |              | VER         | 4               |
|            |              | PROint      | 2               |
|            |              | NOMcom      | 1               |
|            |              | PROind      | 1               |
|            |              | ADVint.neg  | 1               |
| PROint     | 230          | PROrel      | 200             |
|            |              | ADVrel      | 9               |
|            |              | ADVint      | 9               |
|            |              | PROind      | 8               |
|            |              | CONsub      | 2               |
|            |              | PROdem      | 2               |
| ADVint     | 172          | ADVrel      | 94              |
|            |              | CONsub      | 41              |
|            |              | PROrel      | 21              |
|            |              | PROint      | 10              |
|            |              | VER         | 2               |
|            |              | PROper      | 1               |
|            |              | PROind      | 1               |
|            |              | PROref      | 1               |
|            |              | PROdem      | 1               |
| ADJquapro  | 163          | NOMpro      | 163             |
| NOMpro     | 124          | ADJquapro   | 120             |
|            |              | NOMcom      | 4               |
| CONcoo     | 86           | ADV         | 45              |
|            |              | CONsub      | 38              |
|            |              | PROrel      | 2               |
|            |              | NOMcom      | 1               |
| PROdem     | 83           | ADV         | 81              |
|            |              | INJ         | 1               |
|            |              | PROint      | 1               |
| PRE        | 80           | ADV         | 45              |
|            |              | CONsub      | 25              |
|            |              | VER         | 5               |
|            |              | INJ         | 2               |
|            |              | ADJqua      | 2               |
|            |              | ADJord      | 1               |
| PROind     | 69           | PROrel      | 31              |
|            |              | PROint      | 18              |
|            |              | ADV         | 11              |
|            |              | NOMcom      | 7               |
|            |              | ADJqua      | 1               |
|            |              | ADVint      | 1               |
| ADVneg     | 35           | CONsub      | 31              |
|            |              | CONcoo      | 4               |
| ADJord     | 31           | ADJadv.ord  | 13              |
|            |              | ADJqua      | 10              |
|            |              | ADJcar      | 6               |
|            |              | PRE         | 2               |
| PROper     | 22           | PROpos      | 22              |
| PROpos     | 14           | PROper      | 14              |
| INJ        | 14           | PRE         | 7               |
|            |              | VER         | 4               |
|            |              | NOMcom      | 2               |
|            |              | ADJqua      | 1               |
| ADJcar     | 7            | ADV         | 4               |
|            |              | NOMcom      | 3               |
| ADVint.neg | 6            | ADV         | 5               |
|            |              | CONsub      | 1               |
| ADJdis     | 5            | ADJqua      | 2               |
|            |              | ADJord      | 1               |
|            |              | NOMcom      | 1               |
|            |              | ADJcar      | 1               |
| ADJadv.ord | 4            | ADJord      | 4               |
| PROref     | 3            | PROpos.ref  | 3               |
|            | 3            | CONsub      | 1               |
|            |              | ADJqua      | 1               |
|            |              | NOMcom      | 1               |
| PROpos.ref | 2            | PROref      | 2               |
| ADJmul     | 2            | ADJqua      | 2               |

# Voice

[Back to index](#index)

```
all:
  accuracy: 0.992
  precision: 0.972
  recall: 0.9728
  support: 170166
ambiguous-tokens:
  accuracy: 0.9388
  precision: 0.8896
  recall: 0.9011
  support: 14225
unknown-tokens:
  accuracy: 0.963
  precision: 0.9562
  recall: 0.8844
  support: 5916
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 595          | Pass        | 342             |
|          |              | Act         | 176             |
|          |              | Dep         | 71              |
|          |              | SemDep      | 6               |
| Pass     | 365          | _           | 259             |
|          |              | Act         | 80              |
|          |              | Dep         | 25              |
|          |              | SemDep      | 1               |
| Act      | 293          | _           | 213             |
|          |              | Pass        | 72              |
|          |              | Dep         | 8               |
| Dep      | 108          | _           | 59              |
|          |              | Pass        | 38              |
|          |              | Act         | 11              |
| SemDep   | 8            | _           | 7               |
|          |              | Pass        | 1               |

# Mood

[Back to index](#index)

```
all:
  accuracy: 0.9842
  precision: 0.9188
  recall: 0.8946
  support: 170166
ambiguous-tokens:
  accuracy: 0.8868
  precision: 0.8439
  recall: 0.8178
  support: 16578
unknown-tokens:
  accuracy: 0.9446
  precision: 0.7793
  recall: 0.8398
  support: 5916
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Ind      | 744          | Par         | 303             |
|          |              | Sub         | 233             |
|          |              | _           | 148             |
|          |              | Inf         | 54              |
|          |              | Imp         | 4               |
|          |              | SupU        | 1               |
|          |              | Ger         | 1               |
| Par      | 654          | _           | 281             |
|          |              | Ind         | 246             |
|          |              | Inf         | 99              |
|          |              | Sub         | 19              |
|          |              | Imp         | 9               |
| _        | 558          | Par         | 359             |
|          |              | Ind         | 96              |
|          |              | Inf         | 46              |
|          |              | Imp         | 28              |
|          |              | Sub         | 19              |
|          |              | Adj         | 5               |
|          |              | SupUm       | 3               |
|          |              | SupU        | 2               |
| Sub      | 353          | Ind         | 263             |
|          |              | Par         | 48              |
|          |              | _           | 29              |
|          |              | Inf         | 11              |
|          |              | Imp         | 2               |
| Inf      | 289          | Par         | 159             |
|          |              | Ind         | 69              |
|          |              | _           | 49              |
|          |              | Sub         | 8               |
|          |              | Imp         | 4               |
| Imp      | 35           | _           | 18              |
|          |              | Ind         | 6               |
|          |              | Par         | 6               |
|          |              | Inf         | 5               |
| Adj      | 33           | Ger         | 30              |
|          |              | _           | 2               |
|          |              | Ind         | 1               |
| Ger      | 10           | Adj         | 10              |
| SupU     | 8            | Par         | 5               |
|          |              | Inf         | 1               |
|          |              | _           | 1               |
|          |              | Sub         | 1               |
| SupUm    | 6            | _           | 5               |
|          |              | Imp         | 1               |

# Degree

[Back to index](#index)

```
all:
  accuracy: 0.9839
  precision: 0.9758
  recall: 0.9759
  support: 170166
ambiguous-tokens:
  accuracy: 0.934
  precision: 0.9248
  recall: 0.9264
  support: 32038
unknown-tokens:
  accuracy: 0.9501
  precision: 0.9379
  recall: 0.9341
  support: 5916
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Pos      | 1417         | _           | 1414            |
|          |              | Comp        | 3               |
| _        | 1288         | Pos         | 1242            |
|          |              | Sup         | 23              |
|          |              | Comp        | 23              |
| Sup      | 24           | _           | 21              |
|          |              | Pos         | 3               |
| Comp     | 16           | _           | 12              |
|          |              | Sup         | 2               |
|          |              | Pos         | 2               |

# Number

[Back to index](#index)

```
all:
  accuracy: 0.9805
  precision: 0.9794
  recall: 0.9791
  support: 170166
ambiguous-tokens:
  accuracy: 0.928
  precision: 0.9261
  recall: 0.9254
  support: 37273
unknown-tokens:
  accuracy: 0.9572
  precision: 0.9444
  recall: 0.9388
  support: 5916
``` 

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Sing     | 1580         | Plur        | 1015            |
|          |              | _           | 565             |
| Plur     | 1124         | Sing        | 1085            |
|          |              | _           | 39              |
| _        | 610          | Sing        | 567             |
|          |              | Plur        | 43              |

# Person

[Back to index](#index)

```
all:
  accuracy: 0.9928
  precision: 0.9812
  recall: 0.9746
  support: 170166
ambiguous-tokens:
  accuracy: 0.9305
  precision: 0.887
  recall: 0.8713
  support: 12730
unknown-tokens:
  accuracy: 0.9802
  precision: 0.9767
  recall: 0.9643
  support: 5916
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 484          | 3           | 344             |
|          |              | 2           | 82              |
|          |              | 1           | 58              |
| 3        | 483          | _           | 462             |
|          |              | 2           | 11              |
|          |              | 1           | 10              |
| 2        | 154          | _           | 121             |
|          |              | 3           | 24              |
|          |              | 1           | 9               |
| 1        | 103          | _           | 74              |
|          |              | 3           | 26              |
|          |              | 2           | 3               |

# Tense

[Back to index](#index)

```
all:
  accuracy: 0.9886
  precision: 0.6437
  recall: 0.636
  support: 170166
ambiguous-tokens:
  accuracy: 0.9187
  precision: 0.5553
  recall: 0.5278
  support: 16574
unknown-tokens:
  accuracy: 0.9596
  precision: 0.7176
  recall: 0.7144
  support: 5916
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 582          | Perf        | 391             |
|          |              | Pres        | 160             |
|          |              | Fut         | 28              |
|          |              | Pqp         | 3               |
| Perf     | 540          | _           | 301             |
|          |              | Pres        | 138             |
|          |              | Fut         | 60              |
|          |              | Pqp         | 41              |
| Pres     | 418          | _           | 209             |
|          |              | Perf        | 150             |
|          |              | Fut         | 50              |
|          |              | Impa        | 7               |
|          |              | Pqp         | 2               |
| Fut      | 191          | Perf        | 106             |
|          |              | Pres        | 61              |
|          |              | _           | 22              |
|          |              | Pqp         | 1               |
|          |              | Impa        | 1               |
| Pqp      | 163          | Perf        | 157             |
|          |              | _           | 4               |
|          |              | Pres        | 2               |
| PeriPqp  | 14           | Perf        | 11              |
|          |              | _           | 2               |
|          |              | Pqp         | 1               |
| PeriFut  | 14           | Fut         | 10              |
|          |              | Perf        | 3               |
|          |              | _           | 1               |
| PeriPerf | 9            | Perf        | 7               |
|          |              | _           | 2               |
| Impa     | 2            | Pres        | 2               |

# Case

[Back to index](#index)

```
  accuracy: 0.9441
  precision: 0.9064
  recall: 0.8754
  support: 170166
ambiguous-tokens:
  accuracy: 0.8739
  precision: 0.866
  recall: 0.85
  support: 64502
unknown-tokens:
  accuracy: 0.9048
  precision: 0.7741
  recall: 0.7272
  support: 5916
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Nom      | 2743         | Acc         | 1550            |
|          |              | _           | 417             |
|          |              | Abl         | 368             |
|          |              | Gen         | 231             |
|          |              | Voc         | 109             |
|          |              | Dat         | 62              |
|          |              | Ind         | 5               |
|          |              | Loc         | 1               |
| Acc      | 1870         | Nom         | 1276            |
|          |              | _           | 366             |
|          |              | Abl         | 112             |
|          |              | Gen         | 86              |
|          |              | Voc         | 15              |
|          |              | Ind         | 10              |
|          |              | Dat         | 5               |
| Abl      | 1491         | Dat         | 627             |
|          |              | Nom         | 457             |
|          |              | _           | 190             |
|          |              | Acc         | 175             |
|          |              | Gen         | 22              |
|          |              | Voc         | 18              |
|          |              | Ind         | 2               |
| Dat      | 1439         | Abl         | 1110            |
|          |              | Gen         | 224             |
|          |              | Nom         | 70              |
|          |              | _           | 22              |
|          |              | Acc         | 4               |
|          |              | Voc         | 4               |
|          |              | Loc         | 3               |
|          |              | Ind         | 2               |
| _        | 1051         | Nom         | 474             |
|          |              | Acc         | 296             |
|          |              | Abl         | 201             |
|          |              | Dat         | 29              |
|          |              | Gen         | 27              |
|          |              | Ind         | 12              |
|          |              | Voc         | 12              |
| Gen      | 552          | Nom         | 284             |
|          |              | Dat         | 109             |
|          |              | Acc         | 98              |
|          |              | Abl         | 21              |
|          |              | _           | 18              |
|          |              | Voc         | 15              |
|          |              | Loc         | 5               |
|          |              | Ind         | 2               |
| Voc      | 318          | Nom         | 206             |
|          |              | Acc         | 42              |
|          |              | Gen         | 24              |
|          |              | Abl         | 21              |
|          |              | _           | 18              |
|          |              | Dat         | 6               |
|          |              | Loc         | 1               |
| Loc      | 25           | Gen         | 16              |
|          |              | Dat         | 6               |
|          |              | Nom         | 3               |
| Ind      | 24           | _           | 15              |
|          |              | Gen         | 3               |
|          |              | Acc         | 3               |
|          |              | Nom         | 2               |
|          |              | Voc         | 1               |

# Gender

[Back to index](#index)

```
all:
  accuracy: 0.9751
  precision: 0.9393
  recall: 0.9445
  support: 170166
ambiguous-tokens:
  accuracy: 0.9017
  precision: 0.8968
  recall: 0.9058
  support: 35122
unknown-tokens:
  accuracy: 0.938
  precision: 0.8952
  recall: 0.8903
  support: 5916

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 1460         | MascNeut    | 395             |
|          |              | Neut        | 305             |
|          |              | Masc        | 273             |
|          |              | Com         | 210             |
|          |              | Fem         | 208             |
|          |              | MascFem     | 69              |
| Neut     | 965          | Fem         | 334             |
|          |              | _           | 313             |
|          |              | MascNeut    | 280             |
|          |              | Com         | 28              |
|          |              | Masc        | 6               |
|          |              | MascFem     | 4               |
| MascNeut | 616          | _           | 369             |
|          |              | Neut        | 206             |
|          |              | Masc        | 35              |
|          |              | Fem         | 3               |
|          |              | Com         | 2               |
|          |              | MascFem     | 1               |
| Fem      | 509          | Neut        | 302             |
|          |              | _           | 189             |
|          |              | MascFem     | 8               |
|          |              | MascNeut    | 4               |
|          |              | Masc        | 3               |
|          |              | Com         | 3               |
| Masc     | 315          | _           | 202             |
|          |              | MascNeut    | 56              |
|          |              | Com         | 35              |
|          |              | MascFem     | 18              |
|          |              | Neut        | 3               |
|          |              | Fem         | 1               |
| Com      | 272          | _           | 159             |
|          |              | MascFem     | 68              |
|          |              | Masc        | 35              |
|          |              | Neut        | 5               |
|          |              | MascNeut    | 4               |
|          |              | Fem         | 1               |
| MascFem  | 99           | _           | 50              |
|          |              | Com         | 44              |
|          |              | Neut        | 4               |
|          |              | Masc        | 1               |
