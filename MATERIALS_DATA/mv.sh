while read line; do
   cd $line
      #mkdir GAS_PHASE_QM
      #mv ../../DDEC/$line/*log GAS_PHASE_QM
      #mv ../../DDEC/$line/*com GAS_PHASE_QM
      #mkdir DDEC6
      #mv ../../DDEC/$line/job_con* DDEC6
      #mv ../../DDEC/$line/DDEC* DDEC6
      cd GAS_PHASE_QM
      obabel -ilog nN.log -O ${line}.xyz
      cd ..
      mkdir STRUCTURE
      mv GAS_PHASE_QM/${line}.xyz STRUCTURE
   cd ..
done < ./STRUCTURE_LIST
