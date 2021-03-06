![pore_stats logo](https://github.com/tphinkle/pore_stats/blob/master/qt_app/resources/logo.png)


## Contents
1. Overview
2. Event extraction
3. Analysis

## 1. Overview
pore_stats is a software library written in Python for analyzing [resistive pulse](https://en.wikipedia.org/wiki/Tunable_resistive_pulse_sensing) experimental data. The library consists of a GUI program written in PyQt for extracting pulses from the baseline, and modules for analyzing the extracted events.

## 2. Extraction

#### Feature highlights

- Single events are detected and extracted automatically, even from signals with drifting or jagged baselines.

![Events found in baseline](https://github.com/tphinkle/pore_stats/blob/master/qt_app/demo/full_view.png)

- The program allows the user to change the parameters most relevant to the detection algorithm.

- A low-pass filter can be used to reduce noise and find events that are buried in the baseline.

![Hidden events](https://github.com/tphinkle/pore_stats/blob/master/qt_app/demo/filter_demo.png)

#### Event validation

- Detected events can be rejected after detection in one of three ways:

1. Manual accept/reject decision making
	- Commands to scroll through events and accept/reject are bound to simple hot keys that make manual review of the events as fast as possible.

2. Population slicing
	- A region-of-interest (ROI) square can be dragged on the amplitude-duration scatter plot to remove events from regions known to contain undesirable events (e.g., double events with amplitudes that are too large, spurious short-lived noise spikes that were detected as events, etc.)

![Scatter plot view](https://github.com/tphinkle/pore_stats/blob/master/qt_app/demo/scatter_plot_view.png)



3. Machine learning
	- Whenever the event data is saved, the raw data and decision for each event is saved to a separate file. The saved data for all the events constitutes a data set for training a model to make future accept/reject binary decisions on new events. Currently the training data is saved automatically, but the model must be trained manually. After training a model in scikit-learn, it must be pickled and placed in the correct directory for the GUI program to locate it. This method is functional, but will require some hacking to work; unlike the other two methods, this method doesn't work out of the box (for now).

## 3. Analysis

- The pore_stats event analysis libraries can automatically determine the event __amplitude__, __duration__, __local minima and maxima__, and __current levels__ for non-constant pulses.

- Events are loaded in from the file produced by the event extraction program. An RP event is instantiated as an object of type RPEvent, a class that bundles the event's data and methods for performing calculations and transformations on the data.

#### Gallery

Here are some plots of the data created by using the pore_stats analysis library.

<img src="https://github.com/tphinkle/pore_stats/blob/master/qt_app/demo/analysis_gallery/HCT-116_multievent_7-10.png" alt="multievent" height="400"/> <img src="https://github.com/tphinkle/pore_stats/blob/master/qt_app/demo/analysis_gallery/HCT-116_7-29_15um-20um_8-2_scatter.png" alt="scatter" height="400"/>

<img src="https://github.com/tphinkle/pore_stats/blob/master/qt_app/demo/analysis_gallery/event_durations.png" alt="Event durations" height="325"/> <img src="https://github.com/tphinkle/pore_stats/blob/master/qt_app/demo/analysis_gallery/filtered_psmix.png" alt="filtered psmix" height="325"/>

<img src="https://github.com/tphinkle/pore_stats/blob/master/qt_app/demo/analysis_gallery/HCT-116_peak-distributions_7-29_pr0006.png" alt="Peak distributions" height="400"/> 
