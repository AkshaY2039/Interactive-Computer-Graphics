/*
 * utils.js
 * Copyright (C) 2018 g <g@ABCL>
 *
 * Distributed under terms of the MIT license.
 */
"use strict";

function loadScript(url, type, id) {
  var client = new XMLHttpRequest();
  client.open("GET", url, false);
  client.addEventListener("load", function() {
    if (document.getElementById(id) == null) {
      var script = document.createElement("script");
      script.type = type;
      script.id = id;
      script.innerHTML = client.responseText;
      document.head.appendChild(script);
    }
  });
  client.send();
}
