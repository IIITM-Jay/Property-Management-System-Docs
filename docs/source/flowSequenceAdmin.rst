Administration/ Management
=============================================

.. graphviz::
   :align: center

   digraph {
      a->b
      b->c [label="Yes", labelfontcolor=green]
      c->d 
      d->e 
      e->c [label="No", labelfontcolor=green]
      e->f [label="Yes"]
     
     
      a [shape=box, label="Grant Access", peripheries=2,color=lawngreen, fontcolor=white, style=filled, fontcolor=black ]
      b [shape=diamond, label="Admin?" color="lightgray", style=filled]
      c [shape=box, label="DDL, DML, DCL", height=0.25, width=2.5, color=springgreen,style=filled, fontcolor=black ]
      d [shape=box, label="Database", peripheries=2 height=0.25, width=2.5, color=lightblue,style=filled, fontcolor=black ]
      e [shape=diamond, label="Done with the Work?", color=indigo, fontcolor=white, style=filled]
      f [shap=ellipse, peripheries=2,color= orangered, label="Logout", style=filled, fontcolor=white];


      
   }
