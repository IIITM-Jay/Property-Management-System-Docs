Non Admin/ Real World Users
================================================

.. graphviz::
   :align: center

   digraph {
      a->b
      b->c [label="No", labelfontcolor=green]
      c->d 
      d->e 
      e->f
      f->g 
      g->h [label="Yes"]
      g->c [label="No"]
      h->i
      
     
     
      a [shape=box, label="Grant Access", peripheries=2,color=lawngreen, fontcolor=white, style=filled, fontcolor=black ]
      b [shape=diamond, label="Admin?" color="lightgray", style=filled]
      c [shape=box, label="View the Assets/ Properties", height=0.25, width=2.5, color=springgreen,style=filled, fontcolor=black ]
      d [shape=box, label="Search Using Filters", height=0.25, width=2.5, color= olivedrab,style=filled, fontcolor=black ]
      e [shape=box, label="Finish Booking", distortion=0.10, height=0.25, width=2.5, color=lightblue,style=filled, fontcolor=black ]
      f [shape=box, label="Book the property", height=0.25, width=2.5, color= slategray,style=filled, fontcolor=black ]
      g [shape=diamond, label="Confirm Booking?", color=indigo, fontcolor=white, style=filled]
      h [shape=box, label="Reserve", height=0.25, width=0.75, color=chocolate,style=filled, fontcolor=white ]
      i [shap=ellipse, peripheries=2,color= orangered, label="Logout", style=filled, fontcolor=white];


      
   }
