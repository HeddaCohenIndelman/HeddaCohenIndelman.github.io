from jinja2 import Template

# news = [
#      ("fa-newspaper-o",
#       "Our model AudioGen, which generates audio from textual descriptions got some attention from the media: [<a href='https://www.newscientist.com/article/2341416-metas-text-to-audio-ai-can-create-common-sounds-and-generate-music/' target='blank'>New Scientist</a>]."),
#      ("fa-book", "Our research paper <a href='https://arxiv.org/pdf/2111.07402.pdf' target='blank'><em>Textless Speech Emotion Conversion using Decomposed and Discrete Representations</em></a> was accepted to EMNLP 2022!"),
#      ("fa-microphone",
#       "Our model AudioGen, was covered by Aleksa Gordić: [<a href='https://www.youtube.com/watch?v=RyIn-DxGF-c'>YouTube</a>]."),
#      ("fa-book", "4 papers accapted to INTERSPEECH 2022! More details in publications section."),
#      ("fa-book", "Our paper <a href='https://ieeexplore.ieee.org/document/9747953'><em>Speech Time-Scale Modification With GANs</em></a> was accapted to IEEE Signal Processing Letters 2022!"),
#      ("fa-trophy", "Started as a full-time Research Engineer at Meta AI Research"),
#      ("fa-microphone",
#       "Invited talk at <a href='https://homepages.inf.ed.ac.uk/htang2/sigml/seminar/'>ISCA SIGML Seminar<a>, [<a href='https://www.youtube.com/watch?v=gk6thCWl_eE'>Video</a>]."),
# ]

papers = [
{
        "title": "On The Statistical Representation Properties Of The Perturb-Softmax And The Perturb-Argmax Probability Distributions",
        "authors": "<u>Hedda Cohen Indelman</u>, Tamir Hazan",
        "venue": "",
        "links": {
            "PDF,": "https://arxiv.org/pdf/2406.02180",
        },
        "bib": """
@misc{indelman2024statistical,
      title={On The Statistical Representation Properties Of The Perturb-Softmax And The Perturb-Argmax Probability Distributions}, 
      author={Hedda Cohen Indelman and Tamir Hazan},
      year={2024},
      eprint={2406.02180},
      archivePrefix={arXiv},}
            """,
        "year": 2024,
    },
    {
        "title": "Semantic Segmentation Refiner for Ultrasound Applications with Zero-Shot Foundation Models",
        "authors": "<u>Hedda Cohen Indelman</u>, Elay Dahan, Angeles M Perez-Agosto, Carmit Shiran, Doron Shaked, Nati Daniel",
        "venue": "Annual International Conference of the IEEE, Engineering in Medicine and Biology Society (EMBC), 2024",
        "links": {
            "PDF,": "https://arxiv.org/pdf/2404.16325",
        },
        "year": 2024,
        "bib": """
 @misc{indelman2024semantic,
      title={Semantic Segmentation Refiner for Ultrasound Applications with Zero-Shot Foundation Models}, 
      author={Hedda Cohen Indelman and Elay Dahan and Angeles M. Perez-Agosto and Carmit Shiran and Doron Shaked and Nati Daniel},
      year={2024},
      eprint={2404.16325},
      archivePrefix={arXiv},}
        """
    },
    {
        "title": "Learning Latent Partial Matchings with Gumbel-IPF Networks",
        "authors": "<u>Hedda Cohen Indelman</u>, Tamir Hazan",
        "venue": "International Conference on Artificial Intelligence and Statistics (AISTATS), 2024",
        "links": {
            "PDF,": "https://proceedings.mlr.press/v238/cohen-indelman24a/cohen-indelman24a.pdf",
            "Code,": "https://github.com/HeddaCohenIndelman/Learning-Latent-Partial-Matchings-with-Gumbel-IPF-Networks"
        },
        "bib": """
@InProceedings{pmlr-v238-cohen-indelman24a,
  title = 	 { Learning Latent Partial Matchings with {G}umbel-{IPF} Networks },
  author =       {Cohen Indelman, Hedda and Hazan, Tamir},
  booktitle = 	 {Proceedings of The 27th International Conference on Artificial Intelligence and Statistics},
  pages = 	 {1513--1521},
  year = 	 {2024},
  editor = 	 {Dasgupta, Sanjoy and Mandt, Stephan and Li, Yingzhen},
  volume = 	 {238},
  series = 	 {Proceedings of Machine Learning Research},
  month = 	 {02--04 May},
  publisher =    {PMLR}}
            """,
        "year": 2024,
    },
    {
        "title": "InDi: Informative and Diverse Sampling for Dense Retrieval",
        "authors": "Nachshon Cohen, <u>Hedda Cohen Indelman</u>, Yaron Fairstein, Guy Kushilevitz",
        "venue": " European Conference on Information Retrieval, (ECIR), 2024",
        "links": {
            "PDF,": "https://assets.amazon.science/39/b7/5ce986a64af6a9c21d163aedf307/indi-informative-and-diverse-sampling-for-dense-retrieval.pdf",
        },
        "bib": """
        @InProceedings{10.1007/978-3-031-56063-7_16,
    author="Cohen, Nachshon
    and Cohen-Indelman, Hedda
    and Fairstein, Yaron
    and Kushilevitz, Guy",
    title="InDi: Informative and Diverse Sampling for Dense Retrieval",
    booktitle="Advances in Information Retrieval",
    year="2024",
    publisher="Springer Nature Switzerland",
    pages="243--258",
    isbn="978-3-031-56063-7"
    }
        """,
        "year": 2024,
    },
    {
        "title": "Learning Constrained Structured Spaces with Application to Multi-Graph Matching",
        "authors": "<u>Hedda Cohen Indelman</u>, Tamir Hazan",
        "venue": "International Conference on Artificial Intelligence and Statistics (AISTATS), 2023",
        "links": {
            "PDF,": "https://proceedings.mlr.press/v206/indelman23a/indelman23a.pdf",
            "Code,":"https://github.com/HeddaCohenIndelman/Learning-Constrained-Structured-Spaces-with-Application-to-Multi-Graph-Matching"
        },
        "bib": """
        
@InProceedings{pmlr-v206-indelman23a,
  title = 	 {Learning Constrained Structured Spaces with Application to Multi-Graph Matching},
  author =       {Indelman, Hedda Cohen and Hazan, Tamir},
  booktitle = 	 {Proceedings of The 26th International Conference on Artificial Intelligence and Statistics},
  pages = 	 {2589--2602},
  year = 	 {2023},
  editor = 	 {Ruiz, Francisco and Dy, Jennifer and van de Meent, Jan-Willem},
  volume = 	 {206},
  series = 	 {Proceedings of Machine Learning Research},
  month = 	 {25--27 Apr},
  publisher =    {PMLR},}
        """,
        "year": 2023,
    },
    {
        "title": "Learning randomly perturbed structured predictors for direct loss minimization",
        "authors": "<u>Hedda Cohen Indelman</u>, Tamir Hazan",
        "venue": "International Conference on Machine Learning (ICML), 2021",
        "links": {
            "PDF,": "https://proceedings.mlr.press/v139/indelman21a/indelman21a.pdf",
            "Code,": "https://github.com/HeddaCohenIndelman/PerturbedStructuredPredictorsDirect"
        },
        "bib": """
@InProceedings{pmlr-v139-indelman21a,
  title = 	 {Learning Randomly Perturbed Structured Predictors for Direct Loss Minimization},
  author =       {Indelman, Hedda Cohen and Hazan, Tamir},
  booktitle = 	 {Proceedings of the 38th International Conference on Machine Learning},
  pages = 	 {4585--4595},
  year = 	 {2021},
  editor = 	 {Meila, Marina and Zhang, Tong},
  volume = 	 {139},
  series = 	 {Proceedings of Machine Learning Research},
  month = 	 {18--24 Jul},
  publisher =    {PMLR},}
        """,
        "year": 2021,
    },

]

with open("index_template.html", "r") as f:
    site = Template(f.read())

for paper in papers:
    paper["authors"] = paper["authors"].replace("Itai Gat", "<u>Itai Gat</u>")

site = site.render(papers=papers)

with open("index.html", "w") as f:
    f.write(site)
