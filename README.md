# ttmik scripts

Scripts and files for [Talk to me in Korean](https://talktomeinkorean.com), especially the import of their materials into [Anki](https://ankiweb.net/decks/) (flash) cards.

Here's the process, with Level 1 for example:

- I went through the [course lessons](https://talktomeinkorean.com/curriculum/level-1-korean-grammar) manually and recorded the vocab/conversations that I found useful/interesting into `level1.txt`. This is done manually.
- I used ChatGPT/GPT-4 to help me create romanization for me where TTMIK does not provide it, thanks GPT-4!
- I run `python compile.py` to create `level1_compiled.txt`
- I import `level1_compiled.txt` into [Anki](https://ankiweb.net/decks/)
- I study cards to become 한국어 전문가

Feel free to adjust to your needs.

### License

MIT
