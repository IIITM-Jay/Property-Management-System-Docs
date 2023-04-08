Flow Sequence
======================


.. graphviz::
   :align: center

   digraph {
      a->b
      b->d [label="Yes", labelfontcolor=green]
      b->c [label="No", labelfontcolor=red]
      d->c 
      c->e
      e->f [label="Yes"]
      e->g [label="No"]
      g->c
      a [shap=ellipse, peripheries=2,color= lightseagreen, label="Property Management System", style=filled, fontcolor=white];
      b [shape=diamond, label="New User"]
      c [shape=box, label="Login", height=0.25, width=1.5 ]
      d [shape=box, label="Register", height=0.25, width=2 ]
      e [shape=diamond, label="Authorised"]
      f [shape=box, label="Grant Access"]
      g [shape=box, label="Check Your Credentials", height=0.25, width=2 ]


      
   }
