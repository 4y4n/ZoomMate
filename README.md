# ZoomOpener
## Automatic Zoom Opener for class
Don't edit the python file, edit the JSON to your liking instead!
- Make sure to turn on Auto turn off camera and mic in zoom settings beforehand.
- To use: Simply run the `zoomOpener.py` file with the `classData.json` on the same directory level. Don't close the program until your last class opens.
### classData file:
- Structured like so:

```
{
    "name": "[NAME OF CLASS]",
    "link": "[ZOOM LINK]",
    "startTime": "[HOUR CLASS STARTS]",
    "endTime": "[MINUTE CLASS STARTS]",
    "classActive": "[DAYS CLASS IS RUNNING]"
}
```
- Make sure to add each class in order from start of the day to the end.
## startTime & endTime field:
- Starting and ending time for the class string format.
- Meant to be in 24h time.

## classActive field
- Meant to map out which days the class is running. Add the days in short form.
