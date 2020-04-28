#!/usr/bin/env python
# -*- coding: utf-8 -*-

from browser import document

def calc_bmi(ctx):
  weight = float(document["weight"].value)
  height = float(document["height"].value)

  bmi = str(weight/(height*height))
  rslt = document["result"]
  rslt.text = bmi
  log(str(bmi))

execute_btn = document["execute"]
execute_btn.bind("click", calc_bmi)
