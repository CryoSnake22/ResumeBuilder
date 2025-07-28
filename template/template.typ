#import "lib/main_preset.typ":*
#set enum(numbering:"1.")
#set page(margin: 1.5cm)
#set text(
  font: "CMU Serif",
  size:10pt
)
#set raw(theme: "halcyon.tmTheme")
#show raw: it => block(
  fill: rgb("#1d2433"),
  inset: 8pt,
  radius: 5pt,
  text(fill: rgb("#a2aabc"), it)
)

= Polysume:
*1. *The pipeline essentially goes as follows. We start by inputting a pdf file into the script:
#figure(
  image("p1.png", width: auto, height: auto),
  caption: [Possible input],
) <fimg-label>


*2. *The input gets parsed to plain text:

```md
Charles-Antoine Pouliot
Mobile: 581-996-7900
Email: capdev22@gmail.com

Introduction

Languages: French, English
Github

An aspiring software engineer with a diverse background and a love for learning looking for experience 
wherever and whenever possible.

Education and Certifications

University of Ottawa
Bachelor’s of Mathematics

Cégep de Sainte-Foy
Music, Jazz piano

Comptia A+ Certification
-------------------------
ETC...
```
Then the input gets sent to OpenAI api which turns it into YAML
```YAML
name: Charles-Antoine Pouliot

contact:
  email: capdev22@gmail.com
  phone: 581-996-7900

summary: |
  Passionate software engineer with a strong foundation in mathematics and computer science, eager to leverage skills in React and Next.js development to enhance user experiences and drive technological innovation.

education:
  - degree: Dual Bachelor's Degree, Honours Mathematics and Honours Computer Science (Data Science)
    school: University of Ottawa
  - degree: Music, Jazz piano
    school: Cégep de Sainte-Foy
--------------------------
ETC...
```
This finally goes into a latex template generating a final .tex file:

```tex
\begin{onecolentry}
    Passionate software engineer with a strong foundation in mathematics and computer science, eager to leverage skills in React and Next.js development to enhance user experiences and drive technological innovation.

\end{onecolentry}

\section{Education}
\begin{twocolentry}{%
\textit{ }\textit{} \\[0.1cm]
\textit{}%
}
    \textbf{University of Ottawa }\\
    \textit{Dual Bachelor's Degree, Honours Mathematics and Honours Computer Science (Data Science) }\end{twocolentry}
\vspace{0.10 cm}
\begin{twocolentry}{%
\textit{ }\textit{} \\[0.1cm]
\textit{}%
}
    \textbf{Cégep de Sainte-Foy }\\
    \textit{Music, Jazz piano }\end{twocolentry}
\vspace{0.10 cm}

\section{Experience}
\begin{twocolentry}{%
\textit{September 2024 }\textit{} \\[0.1cm]
\textit{Ottawa, ON}%
}
    \textbf{Web Developer/Designer }\\
    \textit{Laurier Computers }
\end{twocolentry}
\vspace{0.10 cm}
\begin{onecolentry}
    \begin{highlights}
        \item Enhanced user experience and scalability by designing and developing the company’s website using Next.js and React.
        \item Improved client satisfaction through effective technical support and timely issue resolution.
    \end{highlights}
\end{onecolentry}
\vspace{0.2 cm}
\begin{twocolentry}{%
\textit{December 2023 }--\textit{August 2024} \\[0.1cm]
\textit{Ottawa, ON}%
}
    \textbf{Server and Concierge }\\
    \textit{Amica the Glebe }
\end{twocolentry}
-------------------------
ETC...
```
Which then gets rendered into the final product:
#figure(
  image("p3.png", width: auto, height: auto),
  caption: [Final Rendered PDF],
) <fimg-label>    

This is still incomplete in its features but I'm quite proud of how it turned out.
