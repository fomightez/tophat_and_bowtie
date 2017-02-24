TopHat2 and Bowtie compatibility
=================================


Relevancy
---------

This has been a relevant concern over the years as evidenced by [here](https://www.biostars.org/p/154060/), [here](http://genomebio.org/not-having-fun-with-tophat/), [here](http://seqanswers.com/forums/showthread.php?t=41254), [here](https://groups.google.com/forum/#!topic/tuxedo-tools-users/vG5Rn0IgxoA), [here](https://www.biostars.org/p/132408/), [here](https://ccb.jhu.edu/software/tophat/index.shtml), [here](http://seqanswers.com/forums/showthread.php?t=24676), and etc., and continues to be as Tophat usage persists (for example, [Wang et al. 2016 PMID: 26483013](https://www.ncbi.nlm.nih.gov/pubmed/26483013); [Jin et al. 2017 PMID: 28166730](https://www.ncbi.nlm.nih.gov/pubmed/28166730), etc.) despite there being a successor program [HISAT2](http://ccb.jhu.edu/software/hisat2/index.shtml) to which the site for Tophat directs current interested parties.

> "Please note that TopHat has entered a low maintenance, low support stage as it is now largely superseded by HISAT2 which provides the same core functionality (i.e. spliced alignment of RNA-Seq reads), in a more accurate and much more efficient way." (Source: https://ccb.jhu.edu/software/tophat/index.shtml)

 Additionally, those interested in replicating the studies of others often face the issue of not being provided information on the versions used in published analyses, and knowledge of some of the working combinations would serve as at least an entry point.




Table Summarizing TopHat2 and Bowtie Compatibility
---------------------------------------------------

<table>
  <tr>
    <td colspan="2">Compatible</td>
    <td colspan="2">NOT compatible</td>
  </tr>
  <tr>
    <td>TopHat2</td>
    <td>Bowtie</td>
    <td>TopHat2</td>
    <td>Bowtie</td>
  </tr>
  <tr>
    <td><a href="http://ccb.jhu.edu/software/tophat/downloads/tophat-2.1.1.Linux_x86_64.tar.gz">v2.1.1 release 2/23/2016</a></td>
    <td><a href="http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.3/bowtie2-2.2.3-linux-x86_64.zip">v2.2.3</a><sup>a</sup></td>
    <td>v2.1.1 release 2/23/2016</td>
    <td>v2.3.0<sup>b</sup></td>
  </tr>
  <tr>
    <td><a href="http://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.12.Linux_x86_64.tar.gz">v2.0.12 release 6/24/2014</a></td>
    <td><a href="http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.3/bowtie2-2.2.3-linux-x86_64.zip">v2.2.3</a><sup>c</sup></td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td><a href="http://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.11.Linux_x86_64.tar.gz">v2.0.11 release 3/4/2014</a></td>
    <td><a href="http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.1/bowtie2-2.2.1-linux-x86_64.zip">v2.2.1</a><sup>*</sup><sup>c</sup></td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td><a href="http://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.11.Linux_x86_64.tar.gz">v2.0.11 release 3/4/2014</a></td>
    <td><a href="http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.1.0/bowtie2-2.1.0-linux-x86_64.zip">v2.1.0</a><sup>+</sup><sup>d</sup></td>
    <td>v2.0.11 release 3/4/2014</td>
    <td>v2.2.2.0<sup>d</sup></td>
  </tr>
   <tr>
    <td><a href="http://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.8.Linux_x86_64.tar.gz">v2.0.8 release 2/26/2013</a></td>
    <td><a href="http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.1.0/bowtie2-2.1.0-linux-x86_64.zip">v2.1.0</a><sup>c</sup></td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td><a href="http://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.8b.Linux_x86_64.tar.gz">v2.0.8b release 4/12/2013</a></td>
    <td><a href="https://sourceforge.net/projects/bowtie-bio/files/bowtie/1.0.0/bowtie-1.0.0-linux-x86_64.zip">v1.0.0</a><sup>c</sup></td>
    <td> </td>
    <td> </td>
  </tr>

</table>
<sup>a</sup>(Source: My own experience.<sup>#</sup>)
<sup>b</sup>(Source: I found a job with Tophat2 would FAIL at the `Mapping left_kept_reads.m2g_um to genome ...  with Bowtie2` step even with very small paired read sets.<sup>#</sup>)
<sup>c</sup>(Source: https://ccb.jhu.edu/software/tophat/index.shtml)
<sup>#</sup>My personal data specifically references the linux_x86_64 versions.
<sup>*</sup>Although it does not support a 64-bit Bowtie2 index.<sup>c</sup>
<sup>+</sup>Official documentation at https://ccb.jhu.edu/software/tophat/index.shtml suggests TopHat 2.0.11 is compatible with Bowtie2 v2.2.1 and probably best that combination is used.










Compatibility Info from: https://ccb.jhu.edu/software/tophat/index.shtml
-------------------------------------------------------------------------

TopHat 2.0.12 release 6/24/2014 is compatible with Bowtie2 v2.2.3.

TopHat 2.0.11 release 3/4/2014 is compatible with Bowtie2 v2.2.1, although it does not support a 64-bit Bowtie2 index yet.

TopHat 2.0.8 release 2/26/2013 is compatible with Bowtie2 v2.1.0.

TopHat 2.0.8b release 4/12/2013 was released in order to provide compatibility with Bowtie v1.0.0



Other resources of compatibility information
---------------------------------------------

Tophat 2.0.11 coupled with Bowtie2 2.1.0 was reported working (Source: [Kashyap Chhatbar](http://genomebio.org/not-having-fun-with-tophat/) ) (I'd put this other other possibilities heading with a note that official documentation at https://ccb.jhu.edu/software/tophat/index.shtml suggests TopHat 2.0.11 is compatible with Bowtie2 v2.2.1

Tophat 2.0.11 incompatible with Bowtie2 2.2.2.0. It would FAIL at the `Mapping left_kept_reads.m2g_um to genome ... with Bowtie2` step even with very small paired read sets. (Source: https://groups.google.com/forum/#!topic/tuxedo-tools-users/vG5Rn0IgxoA)

I personally found TopHat 2.1.1 release 2/23/2016 incompatible with Bowtie2 2.3.0 release Dec 13, 2016. I found a job with Tophat2 would FAIL at the `Mapping left_kept_reads.m2g_um to genome ...  with Bowtie2` step even with very small paired read sets.<sup>*</sup>

I personally found TopHat 2.1.1 release 2/23/2016 compatible with Bowtie v2.2.3<sup>*</sup>


<sup>*</sup>My personal data specifically references the linux_x86_64 versions.


.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
