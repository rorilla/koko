# Koko: Leveraging Gorilla's Dataset for Semantic API Search

**:rocket: Get API suggestions in seconds!** 
`Koko` bridges the gap between natural language queries and precise API calls without the computational overhead of large LLMs.

**:computer: Quickstart** 

```bash
pip install koko-cli
initialize_koko
```

Give it a spin:

```bash
koko draw me a gorilla
```

**:bookmark_tabs: More about `Koko`:** Learn how semantic search over Gorilla's curated dataset simplifies your API exploration journey. [Learn more](#why-koko)

**:wave: Let's collaborate!** Join our community, contribute, or share feedback. [Issues on GitHub](https://github.com/rorilla/koko/issues).

## Why Koko?

- **Speed & Efficiency**: Swift results with minimal computational overhead.
- **Privacy-Centric**: All operations are local, ensuring data confidentiality.
- **Accuracy**: Direct reference to a rich training dataset minimizes inaccuracies.
- **Leveraging Open-Source**: `Koko` benefits from the open-source dataset of the Gorilla project, ensuring high-quality API suggestions.

## Gorilla and Koko

### Gorilla: Pioneering LLMs for API Interactions

Gorilla harnesses the prowess of Large Language Models (LLMs) to bridge natural language and a diverse array of APIs. With its capacity to cater to over 1,600 API calls, Gorilla exemplifies the transformative potential of LLMs. Moreover, the advent of APIBench underscores Gorilla's commitment to fostering community collaboration and broadening its API repertoire.

### Koko: Streamlined and Efficient API Mapping

Gorilla's methodology, though groundbreaking, brings to light the challenges of deploying hefty LLMs — namely computational demands and possible delays. Such challenges may not resonate with every developer, particularly those inclined towards lightweight or privacy-centric tools. Enter `Koko`.

Capitalizing on semantic search and Gorilla's comprehensive dataset, `Koko` emerges as a sprightly, precise, and privacy-conscious alternative for aligning user queries with the right API calls. Tailored for developers from all walks, `Koko` promises prompt and spot-on API suggestions minus the computational heft.

## License

`Koko` is open-source, under the Apache 2.0 License.

## Citation

If you utilize `Koko` or our datasets, please reference our work:

```text
@software{koko_2023,
  author = {@rorilla},
  title = {Koko: Leveraging Gorilla's Dataset for Semantic API Search},
  year = {2023},
  url = {https://github.com/rorilla/koko}
}
```

## Acknowledgments

We gratefully acknowledge the Gorilla project for their open-source dataset, which `Koko` leverages to provide enhanced semantic search capabilities. If you use `Koko` or benefit from the underlying Gorilla dataset, please cite the Gorilla paper:

```text
@article{patil2023gorilla,
  title={Gorilla: Large Language Model Connected with Massive APIs},
  author={Shishir G. Patil and Tianjun Zhang and Xin Wang and Joseph E. Gonzalez},
  year={2023},
  journal={arXiv preprint arXiv:2305.15334},
} 
```
