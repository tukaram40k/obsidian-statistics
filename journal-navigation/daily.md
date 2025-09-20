# Daily note navigation panel
Using Templater with Moment.js:
```js
#### [[<% moment(tp.file.title, "DD-MM-YYYY").format('YYYY') %>]], [[<% moment(tp.file.title, "DD-MM-YYYY").format('MM-YYYY') %>|<% moment(tp.file.title, "DD-MM-YYYY").format('MMMM') %>]], [[<% moment(tp.file.title, "DD-MM-YYYY").format('YYYY-[W]WW') %>|<% moment(tp.file.title, "DD-MM-YYYY").format('[Week-]WW') %>]]
[[<% tp.date.now("DD-MM-YYYY", -1, tp.file.title, "DD-MM-YYYY") %>|<< <% tp.date.now("DD-MM-YYYY", -1, tp.file.title, "DD-MM-YYYY") %>]] | **<% moment(tp.file.title, "DD-MM-YYYY").format("DD-MM-YYYY") %>** | [[<% tp.date.now("DD-MM-YYYY", 1, tp.file.title, "DD-MM-YYYY") %>|<% tp.date.now("DD-MM-YYYY", 1, tp.file.title, "DD-MM-YYYY") %> >>]]
```
Raw output:
```
#### [[2025]], [[09-2025|September]], [[2025-W38|Week-38]]
[[20-09-2025|<< 20-09-2025]] | **21-09-2025** | [[22-09-2025|22-09-2025 >>]]
```
Formatted output:
#### 2025, September, Week-38
<< 20-09-2025 | **21-09-2025** | 22-09-2025 >>