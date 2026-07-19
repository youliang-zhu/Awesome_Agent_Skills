# Beisen Reference

Use this file for Beisen / Phoenix-style campus recruitment forms, including `*.zhiye.com` pages.

## 360 Campus Observations

- Context: 360 campus form at `360campus.zhiye.com/form`, job page title similar to `360集团校园招聘`.
- Section order observed: 投递意向, 个人信息, 教育经历, 实习经历, 项目经历, 语言能力, 获奖情况, 简历附件, 附件.
- The footer has `暂存`, `取消`, and `预览并提交`. `暂存` saved the draft and returned a toast like `暂存成功，请到「投递记录」中查看`. Do not click `预览并提交` without explicit user authorization.

## Field Behavior

- Plain text inputs and textareas accepted UI Automation `ValuePattern.SetValue`. Repeated-entry card additions rerender the page, so re-identify controls by nearby labels and bounding rectangles after each add.
- Phoenix select controls should be selected through the real candidate UI, not by only writing text into the inner edit. The outer select group usually supports `InvokePattern`.
- Month fields such as education, internship, and project dates open `phoenix-calendar-month-calendar`. Select the target year with `phoenix-calendar-month-panel-prev-year-btn` / `phoenix-calendar-month-panel-next-year-btn`, then invoke the month `DataItem` such as `2月`.
- Full date fields such as award date or earliest internship start date open a date calendar with an inner `phoenix-calendar-input`. Focusing that input, replacing its contents with `YYYY-MM-DD`, and pressing Enter can commit the date.
- `至今` checkboxes can disable the ending date select while the select still visually shows `请选择`. Treat the checkbox `ToggleState=On` plus disabled ending date as valid.

## Area Selector

- Native place and similar city fields use an area panel rather than a simple dropdown.
- Provinces, cities, and counties expose `area-text-label` or radio icons with `InvokePattern`. Invoke the label or icon for each level, for example 湖南省 -> 娄底市 -> 双峰县.
- Leaf selection may only update the panel preview. Look for the panel-local small `确定` button near the lower-right of the area popup and invoke it to commit the value back to the select field.
- If a foreign internship location has no Switzerland/overseas option and the field is optional, skip it or choose the closest `其他` only if it can be cleanly committed. Do not block required fields on optional location precision.

## Required Fields Seen On 360

- Personal information included required fields for name, phone, email, ID, native place, graduation school, highest education, whether available for early internship, and earliest internship start date.
- Resume attachment was marked required, but resume upload remains out of bounds unless the user explicitly authorizes upload in the current conversation.
