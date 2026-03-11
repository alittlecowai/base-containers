require("https").get("https://registry.npmjs.org", function (r) {
  console.log(r.statusCode);
});