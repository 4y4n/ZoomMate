# ZoomOpener
## Automatic Zoom Opener for class
Don't edit the python file, edit the JSON to your liking instead!
- Make sure to toggle on the auto turn off mic and camera options in zoom settings beforehand.
- To use: Simply run the `zoomOpener.py` file with the `classData.json` on the same directory level. Don't close the program until your last class opens.
### classData file:
- Structured like so:

```
{
    "name": "[NAME OF CLASS]",
    "link": "[ZOOM LINK]",
    "startTime": "[TIME CLASS STARTS]",
    "endTime": "[TIME CLASS ENDS]",
    "classActive": "[DAYS CLASS IS RUNNING]"
}
```
- Make sure to add each class in order from start of the day to the end.
## startTime & endTime field:
- Starting and ending time for the class in string format.
- Meant to be in 24h time.

## classActive field
- Meant to map out which days the class is running. Add the days in short form.

## Additional Notes:
- Using Windows Task Scheduler in tandem with a .bat file can automate this program further, not requiring you to run the .py file every morning.
