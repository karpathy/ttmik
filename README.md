# ttmik scripts

Scripts and files for [Talk to me in Korean](https://talktomeinkorean.com), especially the import of their materials into [Anki](https://ankiweb.net/decks/) (flash) cards.

Here's the process:

- I went through the [course lessons](https://talktomeinkorean.com/curriculum/level-1-korean-grammar) manually and recorded the vocab/conversations that I found useful/interesting into `notes.md` markdown file. This is done manually.
- I run `python compile.py` to create `cards.txt`. This takes all the cards in my notes (the lines that contain a = sign indicate this) and creates cards for them, both front->back and back->front directions.
- I import `cards.txt` into [Anki](https://ankiweb.net/decks/)
- I study cards to become 한국어 전문가

Feel free to adjust to your needs, it's just text files.

### License

MIT
