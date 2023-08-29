import itertools

#https://www.periodictable.one/elements/
data = """1	H	Hydrogen	1.0079	0.08988	13.99	20.271	2.2	1766
2	He	Helium	4.0026	0.1786	0.95	4.222		1868
3	Li	Lithium	6.938	0.534	453.65	1603	0.98	1817
4	Be	Beryllium	9.01218	1.85	1560	2742	1.57	1798
5	B	Boron	10.806	2.08	2349	4200	2.04	1808
6	C	Carbon	12.0096	1.821			2.55	3750 BC
7	N	Nitrogen	14.0064	1.251	63.15	77.355	3.04	1772
8	O	Oxygen	15.999	1.429	54.36	90.188	3.44	1771
9	F	Fluorine	18.9984	1.696	53.48	85.03	3.98	1810
10	Ne	Neon	20.1797	0.9002	24.56	27.104		1898
11	Na	Sodium	22.9898	0.968	370.944	1156.09	0.93	1807
12	Mg	Magnesium	24.304	1.738	923	1363	1.31	1755
13	Al	Aluminium	26.9815	2.7	933.47	2743	1.61	1825
14	Si	Silicon	28.084	2.329	1687	3538	1.9	1823
15	P	Phosphorus	30.9738	1.823			2.19	1669
16	S	Sulfur	32.059	2.07	388.36	717.8	2.58	2000 BC
17	Cl	Chlorine	35.446	3.2	171.6	239.11	3.16	1774
18	Ar	Argon	39.792	1.784	83.81	87.302		1894
19	K	Potassium	39.0983	0.862	336.7	1032	0.82	1807
20	Ca	Calcium	40.0784	1.55	1115	1757	1	1808
21	Sc	Scandium	44.9559	2.985	1814	3109	1.36	1879
22	Ti	Titanium	47.8671	4.506	1941	3560	1.54	1791
23	V	Vanadium	50.9415	6	2183	3680	1.63	1801
24	Cr	Chromium	51.9962	7.19	2180	2944	1.66	1794
25	Mn	Manganese	54.938	7.21	1519	2334	1.55	1774
26	Fe	Iron	55.8452	7.874	1811	3134	1.83	5000 BC
27	Co	Cobalt	58.9332	8.9	1768	3200	1.88	1735
28	Ni	Nickel	58.6934	8.908	1728	3003	1.91	1751
29	Cu	Copper	63.5463	8.96	1357.77	2835	1.9	9000 BC
30	Zn	Zinc	65.382	7.14	692.68	1180	1.65	1000 BC
31	Ga	Gallium	69.7231	5.91	302.915	2673	1.81	1875
32	Ge	Germanium	72.6308	5.323	1211.4	3106	2.01	1886
33	As	Arsenic	74.9216	5.727			2.18	815
34	Se	Selenium	78.9718	4.81	494	958	2.55	1817
35	Br	Bromine	79.901	3.1028	265.8	332	2.96	1825
36	Kr	Krypton	83.7982	3.749	115.78	119.93	3	1898
37	Rb	Rubidium	85.4678	1.532	312.45	961	0.82	1861
38	Sr	Strontium	87.621	2.64	1050	1650	0.95	1787
39	Y	Yttrium	88.9058	4.472	1799	3203	1.22	1794
40	Zr	Zirconium	91.2242	6.52	2128	4650	1.33	1789
41	Nb	Niobium	92.9064	8.57	2750	5017	1.6	1801
42	Mo	Molybdenum	95.951	10.28	2896	4912	2.16	1778
43	Tc	Technetium	98.9062	11	2430	4538	1.9	1937
44	Ru	Ruthenium	101.072	12.45	2607	4423	2.2	1844
45	Rh	Rhodium	102.906	12.41	2237	3968	2.28	1804
46	Pd	Palladium	106.421	12.023	1828.05	3236	2.2	1802
47	Ag	Silver	107.868	10.49	1234.93	2435	1.93	5000 BC
48	Cd	Cadmium	112.414	8.65	594.22	1040	1.69	1817
49	In	Indium	114.818	7.31	429.749	2345	1.78	1863
50	Sn	Tin	118.711	7.365	505.08	2875	1.96	3500 BC
51	Sb	Antimony	121.76	6.697	903.78	1908	2.05	815
52	Te	Tellurium	127.603	6.24	722.66	1261	2.1	1782
53	I	Iodine	126.904	4.933	386.85	457.4	2.66	1811
54	Xe	Xenon	131.294	5.894	161.4	165.051	2.6	1898
55	Cs	Cesium	132.905	1.93	301.7	944	0.79	1860
56	Ba	Barium	137.328	3.51	1000	2118	0.89	1772
57	La	Lanthanum	138.905	6.162	1193	3737	1.1	1838
58	Ce	Cerium	140.116	6.77	1068	3716	1.12	1803
59	Pr	Praseodymium	140.908	6.77	1208	3403	1.13	1885
60	Nd	Neodymium	144.242	7.01	1297	3347	1.14	1885
61	Pm	Promethium	145	7.26	1315	3273	1.13	1942
62	Sm	Samarium	150.362	7.52	1345	2173	1.17	1879
63	Eu	Europium	151.964	5.264	1099	1802	1.2	1896
64	Gd	Gadolinium	157.253	7.9	1585	3273	1.2	1880
65	Tb	Terbium	158.925	8.23	1629	3396	1.1	1843
66	Dy	Dysprosium	162.5	8.54	1680	2840	1.22	1886
67	Ho	Holmium	164.93	8.79	1734	2873	1.23	1878
68	Er	Erbium	167.259	9.066	1802	3141	1.24	1843
69	Tm	Thulium	168.934	9.32	1818	2223	1.25	1879
70	Yb	Ytterbium	173.045	6.9	1097	1469	1.1	1878
71	Lu	Lutetium	174.967	9.841	1925	3675	1.27	1906
72	Hf	Hafnium	178.492	13.31	2506	4876	1.3	1922
73	Ta	Tantalum	180.948	16.69	3290	5731	1.5	1802
74	W	Tungsten	183.841	19.25	3695	6203	2.36	1781
75	Re	Rhenium	186.207	21.02	3459	5869	1.9	1908
76	Os	Osmium	190.233	22.59	3306	5285	2.2	1803
77	Ir	Iridium	192.217	22.56	2719	4403	2.2	1803
78	Pt	Platinum	195.085	21.45	2041.4	4098	2.28	1735
79	Au	Gold	196.967	19.3	1337.33	3243	2.54	6000 BC
80	Hg	Mercury	200.592	13.534	234.321	629.88	2	1500 BC
81	Tl	Thallium	204.382	11.85	577	1746	1.62	1861
82	Pb	Lead	207.21	11.34	600.61	2022	1.87	7000 BC
83	Bi	Bismuth	208.98	9.78	544.7	1837	2.02	1000
84	Po	Polonium	209	9.196	527	1235	2	1898
85	At	Astatine	210	6.35	575	610	2.2	1940
86	Rn	Radon	222	9.73	202	211.5	2.2	1899
87	Fr	Francium	223	1.87	300	950	0.79	1939
88	Ra	Radium	226	5.5	1233	2010	0.9	1898
89	Ac	Actinium	227	10	1500	3500	1.1	1902
90	Th	Thorium	232.038	11.724	2023	5061	1.3	1829
91	Pa	Protactinium	231.036	15.37	1841	4300	1.5	1913
92	U	Uranium	238.029	19.1	1405.3	4404	1.38	1789
93	Np	Neptunium	237	20.45	912	4447	1.36	1940
94	Pu	Plutonium	244	19.816	912.5	3505	1.28	1940
95	Am	Americium	243	12	1449	2880	1.13	1944
96	Cm	Curium	247	13.51	1613	3383	1.28	1944
97	Bk	Berkelium	247	14.78	1259	2900	1.3	1949
98	Cf	Californium	251	15.1	1173	1743	1.3	1950
99	Es	Einsteinium	252	8.84	1133	1269	1.3	1952
100	Fm	Fermium	257		1800		1.3	1952
101	Md	Mendelevium	258		1100		1.3	1955
102	No	Nobelium	259		1100		1.3	1966
103	Lr	Lawrencium	262		1900		1.3	1961
104	Rf	Rutherfordium	261	23.2	2400	5800		1969
105	Db	Dubnium	268	29.3				1970
106	Sg	Seaborgium	269	35				1974
107	Bh	Bohrium	270.133	37.1				1981
108	Hs	Hassium	269	40.7	126			1984
109	Mt	Meitnerium	277.154	37.4				1982
110	Ds	Darmstadtium	281	34.8				1994
111	Rg	Roentgenium	281	28.7				1994
112	Cn	Copernicium	285	23.7		3570		1996
113	Nh	Nihonium	286	16	700	1430		2003
114	Fl	Flerovium	289	14	340	420		1999
115	Mc	Moscovium	288	13.5	670	1400		2003
116	Lv	Livermorium	293	12.9	709	1085		2000
117	Ts	Tennessine	294	7.17	723	883		2009
118	Og	Oganesson	294	4.95		350		2002"""

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


if __name__ == "__main__":
    solutions = []
    symbols = []
    for line in data.splitlines():
        num, symbol, name, _, _, _, _, _, _ = line.split('\t')
        symbols.append(symbol)
    
    #number_string = numbers[5]#numbers[1] + numbers[3] + numbers[6]
    #nstrings = [numbers[x] for x in range(0, 10)]
    
    word_combos = list(itertools.permutations(numbers, 5))

    
    nstrings = (''.join(items) for items in word_combos)
    
    for number_string in nstrings:
        
        symbol_string = ''
        remaining_length = len(number_string)
        while remaining_length > 0:
            start_idx = len(number_string) - remaining_length
            # will fail on one letter remaining
            try:
                two = number_string[start_idx:start_idx+2].capitalize()
                #print (f'Two: {two}')
                if (two in symbols):
                    #print (f'Found {two}!')
                    symbol_string += two
                    remaining_length -= 2
                    continue
            except:
                pass
            
            one = number_string[start_idx].capitalize()
            #print (f'One: {two}')
            if (one in symbols):
                #print (f'Found {one}!')
                symbol_string += one
                remaining_length -= 1
                continue
            break
        else:
            #print (f'Solution Found - {symbol_string}')
            solutions.append((number_string, symbol_string))
            continue
        #print (f'No solution found - got to {symbol_string}')
        solutions.append((number_string, symbol_string))
    
    # sort solutions by how close they were in length to the original
    solutions = sorted(solutions, key=lambda x: (len(x[0])-len(x[1])))
        
    # print out solutions
    for prompt, solution in solutions[:20]:
        print (f'{prompt} : {solution}')