Examples
=================================
Basic Usage
-----------
Python Code
~~~~~~~~~~~
.. code-block:: python

    from simpletex import write, save
    from simpletex.document import Document, Section, Subsection
    
    with Document(size='11pt'):
        with Section('Section Name'):
            with Subsection('Subsection Name'):
                write('Hello World!')
    
    save('filename.tex')

TeX Output
~~~~~~~~~~
.. code-block:: tex


	\documentclass[11pt]{article}
	
	\usepackage[utf8]{inputenc}
	
	\begin{document}
		\section{Section Name}
			\subsection{Subsection Name}
				Hello World!
	\end{document}

PDF Output
~~~~~~~~~~
.. image:: /_static/basic.png
   :alt: Generated PDF

Simple List and Text Formatting
-------------------------------
Python Code
~~~~~~~~~~~
.. code-block:: python

	from simpletex import write, save, alias
	from simpletex.document import Document, Section, Subsection
	from simpletex.formatting.text import Bold, Italics, Underline, Emphasis, SmallCaps
	from simpletex.sequences import OrderedList, UnorderedList
	
	UnorderedList.bullet = '>'
	
	with Document(size='11pt'):
	    with Section('Section Name'):
	        with UnorderedList():
	            write(Bold()('Bold Text'))
	            write(Italics()('Italic Text'))
	            write(Underline()('Underlined Text'))
	            with Underline():
	                write('More Underlined Text')
	        with Subsection('Subsection Name'):
	            write('The quick brown fox jumps over the lazy dog.')
	            with OrderedList():
	                write(Emphasis()('Emphasized Text'))
	                write(SmallCaps()('Small Caps'))
	
	save('filename.tex')


TeX Output
~~~~~~~~~~
.. code-block:: tex


	\documentclass[11pt]{article}
	
	\usepackage[utf8]{inputenc}
	
	\begin{document}
		\section{Section Name}
			\begin{itemize}
				\item[>] \textbf{Bold Text}
				\item[>] \textit{Italic Text}
				\item[>] \underline{Underlined Text}
				\item[>] \underline{More Underlined Text}
			\end{itemize}
			\subsection{Subsection Name}
				The quick brown fox jumps over the lazy dog.
				\begin{enumerate}
					\item \emph{Emphasized Text}
					\item \textsc{Small Caps}
				\end{enumerate}
	\end{document}

PDF Output
~~~~~~~~~~
.. image:: /_static/list_formatting.png
   :alt: Generated PDF


XeTeX Support and Fonts
-----------------------

Python Code
~~~~~~~~~~~
.. code-block:: python


    from simpletex import write, write_break, save, usepackage
    from simpletex.document import Document, Section, Subsection
    from simpletex.formatting import Style
    from simpletex.formatting.font import Font
    from simpletex.formatting.text import Centering, Italics, SmallCaps
    
    Title = Style()
    Title.apply(Font('Bebas Neue Bold', size=40))
    
    Subtitle = Style()
    Subtitle.apply(Font('Times New Roman', size=11))
    
    Section.heading.apply(Font('Open Sans Semibold', size=16))
    
    Subsection.heading.apply(Font('Open Sans Semibold', size=12))
    Subsection.heading.apply(Italics())
    Subsection.heading.apply(Centering())
    
    usepackage('geometry', margin='0.5in')
    with Document(size='11pt') as doc:
        with Centering():
            write_break(Title('Example Title Text'))
            with Subtitle:
                write_break("Example Subtitle Text")
                write_break("More Subtitle Text")
        with Section('Section Name'):
            write('Example section text.')
            write(SmallCaps()('Lorem ipsum dolor si amet.'))
            with Subsection('Subsection Name'):
                write('Hello World!')
    
    save('filename.tex')

TeX Output
~~~~~~~~~~
.. code-block:: tex


	\documentclass[11pt]{article}
	
	\usepackage[margin=0.5in]{geometry}
	\usepackage[utf8]{inputenc}
	\usepackage{xltxtra}
	\usepackage{fontspec}
	\usepackage{anyfontsize}
	\usepackage{titlesec}
	
	\newfontfamily\BebasNeueBold[Mapping=tex-text]{Bebas Neue Bold}
	\newfontfamily\TimesNewRoman[Mapping=tex-text]{Times New Roman}
	\newfontfamily\OpenSansSemibold[Mapping=tex-text]{Open Sans Semibold}
	
	\titleformat*{\subsection}{\centering\itshape\fontsize{12}{15}\OpenSansSemibold }
	\titleformat*{\section}{\fontsize{16}{20}\OpenSansSemibold }
	
	\begin{document}
		\begin{center}
			{\fontsize{40}{52}\BebasNeueBold Example Title Text} \\
			{\fontsize{11}{14}\TimesNewRoman Example Subtitle Text \\
			More Subtitle Text \\}
		\end{center}
		\section{Section Name}
			Example section text.
			\textsc{Lorem ipsum dolor si amet.}
			\subsection{Subsection Name}
				Hello World!
	\end{document}


PDF Output
~~~~~~~~~~
.. image:: /_static/font.png
   :alt: Generated PDF
