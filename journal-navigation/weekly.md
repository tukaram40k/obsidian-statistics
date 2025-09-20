# Weekly note navigation panel
Using Templater with Moment.js:
```js
#### [[<% moment(tp.file.title, "YYYY-[W]WW").format('YYYY') %>]], [[<% moment(tp.file.title, "YYYY-[W]WW").startOf('month').format('MM-YYYY') %>|<% moment(tp.file.title, "YYYY-[W]WW").startOf('month').format('MMMM') %>]]
***
[[<% moment(tp.file.title, "YYYY-[W]WW").add(-1, 'weeks').format("YYYY-[W]WW") %>|<< <% moment(tp.file.title, "YYYY-[W]WW").add(-1, 'weeks').format("[Week]-WW") %>]] | **<% moment(tp.file.title, "YYYY-[W]WW").format("[Week]-WW") %>** | [[<% moment(tp.file.title, "YYYY-[W]WW").add(1, 'weeks').format("YYYY-[W]WW") %>|<% moment(tp.file.title, "YYYY-[W]WW").add(1, 'weeks').format("[Week]-WW") %> >>]]
[[<% tp.date.weekday("DD-MM-YYYY", 0, tp.file.title, "YYYY-[W]WW") %>|<% tp.date.weekday("dddd", 0, tp.file.title, "YYYY-[W]WW") %>]] - [[<% tp.date.weekday("DD-MM-YYYY", 1, tp.file.title, "YYYY-[W]WW") %>|<% tp.date.weekday("dddd", 1, tp.file.title, "YYYY-[W]WW") %>]] - [[<% tp.date.weekday("DD-MM-YYYY", 2, tp.file.title, "YYYY-[W]WW") %>|<% tp.date.weekday("dddd", 2, tp.file.title, "YYYY-[W]WW") %>]] - [[<% tp.date.weekday("DD-MM-YYYY", 3, tp.file.title, "YYYY-[W]WW") %>|<% tp.date.weekday("dddd", 3, tp.file.title, "YYYY-[W]WW") %>]] - [[<% tp.date.weekday("DD-MM-YYYY", 4, tp.file.title, "YYYY-[W]WW") %>|<% tp.date.weekday("dddd", 4, tp.file.title, "YYYY-[W]WW") %>]] - [[<% tp.date.weekday("DD-MM-YYYY", 5, tp.file.title, "YYYY-[W]WW") %>|<% tp.date.weekday("dddd", 5, tp.file.title, "YYYY-[W]WW") %>]] - [[<% tp.date.weekday("DD-MM-YYYY", 6, tp.file.title, "YYYY-[W]WW") %>|<% tp.date.weekday("dddd", 6, tp.file.title, "YYYY-[W]WW") %>]]
```
Raw output:
```
#### [[2025]], [[09-2025|September]]
***
[[2025-W37|<< Week-37]] | **Week-38** | [[2025-W39|Week-39 >>]]
[[15-09-2025|Monday]] - [[16-09-2025|Tuesday]] - [[17-09-2025|Wednesday]] - [[18-09-2025|Thursday]] - [[19-09-2025|Friday]] - [[20-09-2025|Saturday]] - [[21-09-2025|Sunday]]
```
Formatted output:
#### 2025, September
***
<< Week-37 | **Week-38** | Week-39 >>

Monday - Tuesday - Wednesday - Thursday - Friday - Saturday - Sunday