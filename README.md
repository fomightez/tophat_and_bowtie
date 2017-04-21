TopHat2 and Bowtie compatibility
=================================


Relevancy
---------

This has been a relevant concern over the years as evidenced by [here](https://www.biostars.org/p/154060/), [here](http://genomebio.org/not-having-fun-with-tophat/), [here](http://seqanswers.com/forums/showthread.php?t=41254), [here](https://groups.google.com/forum/#!topic/tuxedo-tools-users/vG5Rn0IgxoA), [here](https://www.biostars.org/p/132408/), [here](https://ccb.jhu.edu/software/tophat/index.shtml), [here](http://seqanswers.com/forums/showthread.php?t=24676), and etc., and continues to be as Tophat usage persists (for example, [Wang et al. 2016 PMID: 26483013](https://www.ncbi.nlm.nih.gov/pubmed/26483013); [Jin et al. 2017 PMID: 28166730](https://www.ncbi.nlm.nih.gov/pubmed/28166730), etc.) despite there being a successor program [HISAT2](http://ccb.jhu.edu/software/hisat2/index.shtml) to which the site for Tophat directs current interested parties.

> "Please note that TopHat has entered a low maintenance, low support stage as it is now largely superseded by [HISAT2](http://ccb.jhu.edu/software/hisat2/index.shtml) which provides the same core functionality (i.e. spliced alignment of RNA-Seq reads), in a more accurate and much more efficient way." (Source: https://ccb.jhu.edu/software/tophat/index.shtml)

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
    <td><a href="http://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.12.Linux_x86_64.tar.gz">v2.0.14 release 3/24/2015</a><sup>Best for Macs(?)</sup><sup>a</sup><sup>c</sup></td>
    <td><a href="http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.3/bowtie2-2.2.3-linux-x86_64.zip">v2.2.3</a><sup>d</sup></td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td><a href="http://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.12.Linux_x86_64.tar.gz">v2.0.12 release 6/24/2014</a></td>
    <td><a href="http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.3/bowtie2-2.2.3-linux-x86_64.zip">v2.2.3</a><sup>d</sup></td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td><a href="http://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.11.Linux_x86_64.tar.gz">v2.0.11 release 3/4/2014</a></td>
    <td><a href="http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.1/bowtie2-2.2.1-linux-x86_64.zip">v2.2.1</a><sup>*</sup><sup>d</sup></td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td><a href="http://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.11.Linux_x86_64.tar.gz">v2.0.11 release 3/4/2014</a></td>
    <td><a href="http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.1.0/bowtie2-2.1.0-linux-x86_64.zip">v2.1.0</a><sup>+</sup><sup>e</sup></td>
    <td>v2.0.11 release 3/4/2014</td>
    <td>v2.2.2.0<sup>e</sup></td>
  </tr>
  <tr>
    <td><a href="http://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.9.Linux_x86_64.tar.gz">v2.0.9 release 6/28/2013</a><sup>f</sup></td>
    <td><a href="http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.1.0/bowtie2-2.1.0-linux-x86_64.zip">v2.1.0-2</a><sup>d</sup></td>
    <td> </td>
    <td> </td>
  </tr>
   <tr>
    <td><a href="http://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.8.Linux_x86_64.tar.gz">v2.0.8 release 2/26/2013</a></td>
    <td><a href="http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.1.0/bowtie2-2.1.0-linux-x86_64.zip">v2.1.0</a><sup>d</sup></td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td><a href="http://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.8b.Linux_x86_64.tar.gz">v2.0.8b release 4/12/2013</a></td>
    <td><a href="https://sourceforge.net/projects/bowtie-bio/files/bowtie/1.0.0/bowtie-1.0.0-linux-x86_64.zip">v1.0.0</a><sup>d</sup></td>
    <td> </td>
    <td> </td>
  </tr>

</table>
<sup>a</sup>Source: My own experience.<sup>#</sup></br>  
<sup>b</sup>Source: I found a job with Tophat2 would FAIL at the `Mapping left_kept_reads.m2g_um to genome ...  with Bowtie2` step even with very small paired read sets.<sup>#</sup></br>    
<sup>c</sup>Source: Attempts with TopHat2 v2.1.1 on Mac OSX resulted in failure at the `Searching for junctions via segment mapping` step, specifically `Error: segment-based junction search failed with err =-5`. I didn't have this error when I changed to using TopHat2 v2.0.14 on Mac OSX, and instead the job worked, see the 'Tophat2 on Mac' section for more details.</a> </br>   
<sup>d</sup>Source: <a href="https://ccb.jhu.edu/software/tophat/index.shtml">https://ccb.jhu.edu/software/tophat/index.shtml</a></br>    
<sup>e</sup>Source: <a href="https://groups.google.com/d/msg/tuxedo-tools-users/vG5Rn0IgxoA/PQ-JHh29oMoJ">https://groups.google.com/d/msg/tuxedo-tools-users/vG5Rn0IgxoA/PQ-JHh29oMoJ</a>  </br>  
<sup>f</sup> Source: It has been suggested by a colleague, Md Shafiuddin, that for Unix flavors with `apt-get` you can simply run `apt-get install - y tophat` and it will also get a compatible version of Bowtie automatically as part of install process, see [here](http://installion.co.uk/ubuntu/vivid/universe/t/tophat/install/index.html) says it is Tophat2. These seem to be versions Tophat2 2.0.9 and Bowtie 2.1.0-2. NOTE: I found I had to run `sudo apt-get update` for `apt-get` to see the package from inside a standard Ubuntu 14.04 Docker image.  </br>  
<sup>#</sup>My personal data specifically references the linux_x86_64 versions, with the important exception of TopHat2 v2.0.14 information, which was on a Mac, see footnote c.  </br>  
<sup>*</sup>Although it does not support a 64-bit Bowtie2 index.<sup>c</sup>  </br>  
<sup>+</sup>Official documentation at <a href="https://ccb.jhu.edu/software/tophat/index.shtml">https://ccb.jhu.edu/software/tophat/index.shtml</a> suggests TopHat 2.0.11 is compatible with Bowtie2 v2.2.1 and probably best that combination is used.  </br>  





Tophat2 on Mac
--------------

When I tried running TopHat version 2.1.1 on a Mac OSX 10.9.5 computer recently, I had it fail at a specific point with a specific error.

    Searching for junctions via segment mapping
        [FAILED]
    Error: segment-based junction search failed with err =-5
      Reason: image not found

Others had seen this happen as well and they were all running on OSX as far as I can tell, see [here](https://www.biostars.org/p/191081/) and [here](https://www.biostars.org/p/194771/). [In one case it had been tracked to a library not being loaded correctly](https://www.biostars.org/p/191081/). In lieu of a soltuion, I can offer a work-around. I found that moving back to TopHat2 version 2.0.14 worked, as [moving back to version 2.0.13 had been reported to work by others](https://www.biostars.org/p/191081/).





Older Tophat2 on Ubuntu
-----------------------

It has been suggested by a colleague, Md Shafiuddin, that if you don't mind an older verison of Tophat2, for Unix flavors with `apt-get` you can simply run `apt-get install - y tophat` and it will also get a compatible version of Bowtie automatically as part of install process. Despite the name used in the `apt-get` statement, [here](http://installion.co.uk/ubuntu/vivid/universe/t/tophat/install/index.html) says it is Tophat2. These seem to be versions Tophat2 2.0.9 and Bowtie 2.1.0-2. NOTE: I found I had to run `sudo apt-get update` to get `apt-get` to see the package from inside a standard Ubuntu 14.04 Docker image.




Compatibility Info from: https://ccb.jhu.edu/software/tophat/index.shtml
-------------------------------------------------------------------------

TopHat 2.0.12 release 6/24/2014 is compatible with Bowtie2 v2.2.3.

TopHat 2.0.11 release 3/4/2014 is compatible with Bowtie2 v2.2.1, although it does not support a 64-bit Bowtie2 index yet.

TopHat 2.0.8 release 2/26/2013 is compatible with Bowtie2 v2.1.0.

TopHat 2.0.8b release 4/12/2013 was released in order to provide compatibility with Bowtie v1.0.0



Other resources of compatibility information
---------------------------------------------

Tophat 2.0.11 coupled with Bowtie2 2.1.0 was reported working (Source: [Kashyap Chhatbar](http://genomebio.org/not-having-fun-with-tophat/) )

Tophat 2.0.11 incompatible with Bowtie2 2.2.2.0. It would FAIL at the `Mapping left_kept_reads.m2g_um to genome ... with Bowtie2` step even with very small paired read sets. (Source: https://groups.google.com/forum/#!topic/tuxedo-tools-users/vG5Rn0IgxoA)

I personally found TopHat 2.1.1 release 2/23/2016 incompatible with Bowtie2 2.3.0 release Dec 13, 2016. I found a job with Tophat2 would FAIL at the `Mapping left_kept_reads.m2g_um to genome ...  with Bowtie2` step even with very small paired read sets.<sup>*</sup>

I personally found TopHat 2.1.1 release 2/23/2016 compatible with Bowtie v2.2.3<sup>*</sup>

I personally found TopHat 2.0.14 release 2/23/2016 compatible with Bowtie v2.2.3<sup>*</sup>


<sup>*</sup>My personal data specifically references the linux_x86_64 versions, except in the case of TopHat 2.0.14 release 2/23/2016 compatible with Bowtie v2.2.3 infromation was from a Mac where TopHat 2.1.1 had resulted in an error, see the 'Tophat2 on Mac' section for details.

Related
-------

[Bioinformatics Software Compatibility](http://bioinformatics-software-compatibility.readthedocs.io/en/latest/)
