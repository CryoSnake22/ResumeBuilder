
#let hello = "hello there"

#let theorem(title, body) = block[
  #text(bold)[Theorem. #title]
  #body
]
